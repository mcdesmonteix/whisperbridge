let userId = null;
let userLang = null;
let ws = null;
let mediaRecorder = null;
let audioChunks = [];

// Sur mobile, TTS désactivé par défaut (nécessite un geste utilisateur sur iOS)
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
let ttsEnabled = !isMobile;
let ttsUnlocked = false;

// VAD (Voice Activity Detection)
const VAD_THRESHOLD    = 18;    // Sensibilité (0-255) — augmenter si trop sensible
const VAD_SILENCE_DELAY = 1500; // ms de silence avant envoi
const VAD_MAX_DURATION  = 30000; // 30s max par enregistrement

let vadActive      = false;
let vadStream      = null;
let vadAudioCtx    = null;
let vadAnalyser    = null;
let vadDetecting   = false;
let vadSpeaking    = false;
let vadSilenceTimer = null;
let vadMaxTimer    = null;

const USERS = {
  louise: { lang: "fr", flag: "🇫🇷", label: "Louise", ttsLang: "fr-FR" },
  olivia: { lang: "en", flag: "🇺🇸", label: "Olivia", ttsLang: "en-US" },
};

// ── Connexion ──

function connect(id) {
  userId   = id;
  userLang = USERS[id].lang;

  document.getElementById("screen-select").classList.add("hidden");
  document.getElementById("screen-chat").classList.remove("hidden");

  updateTTSButton();
  updateVADButton();

  const protocol = location.protocol === "https:" ? "wss:" : "ws:";
  ws = new WebSocket(`${protocol}//${location.host}/ws/${userId}`);

  ws.onopen  = () => { addSystemMessage("Connexion établie ✓"); requestMicPermission(); };
  ws.onclose = () => addSystemMessage("Déconnecté du serveur.");
  ws.onerror = () => addSystemMessage("Erreur de connexion.");

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.type === "status") {
      updateStatus(msg.user, msg.online);
      const info = USERS[msg.user];
      addSystemMessage(msg.online
        ? `${info.flag} ${info.label} est connecté(e)`
        : `${info.flag} ${info.label} s'est déconnecté(e)`);
    }
    if (msg.type === "message") {
      addMessage(msg);
      if (msg.user !== userId && ttsEnabled) speak(msg.translated, USERS[userId].ttsLang);
    }
  };
}

// ── Statut ──

function updateStatus(user, online) {
  const dot = document.getElementById(`status-${user}`);
  if (!dot) return;
  dot.classList.toggle("online",  online);
  dot.classList.toggle("offline", !online);
}

// ── Messages ──

function addSystemMessage(text) {
  const div = document.createElement("div");
  div.className   = "msg-system";
  div.textContent = text;
  appendToMessages(div);
}

function addMessage(msg) {
  const isMe    = msg.user === userId;
  const info    = USERS[msg.user];
  const mainText = isMe ? msg.original  : msg.translated;
  const subText  = isMe ? msg.translated : msg.original;

  const wrapper = document.createElement("div");
  wrapper.className = `message ${isMe ? "me" : "other"}`;

  const bubble = document.createElement("div");
  bubble.className   = "message-bubble";
  bubble.textContent = mainText;

  const translation = document.createElement("div");
  translation.className   = "message-translation";
  translation.textContent = `→ ${subText}`;

  const meta = document.createElement("div");
  meta.className   = "message-meta";
  meta.textContent = `${info.flag} ${info.label} · ${msg.timestamp}`;

  wrapper.appendChild(bubble);
  wrapper.appendChild(translation);
  wrapper.appendChild(meta);
  appendToMessages(wrapper);
}

function appendToMessages(el) {
  const c = document.getElementById("messages");
  c.appendChild(el);
  c.scrollTop = c.scrollHeight;
}

// ── TTS ──

function speak(text, lang) {
  if (!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const utt = new SpeechSynthesisUtterance(text);
  utt.lang = lang;
  utt.rate = 0.95;
  window.speechSynthesis.speak(utt);
}

function unlockTTS() {
  if (!ttsUnlocked && window.speechSynthesis) {
    const u = new SpeechSynthesisUtterance(" ");
    u.volume = 0;
    window.speechSynthesis.speak(u);
    ttsUnlocked = true;
  }
}

function toggleTTS() {
  ttsEnabled = !ttsEnabled;
  if (!ttsEnabled) window.speechSynthesis?.cancel();
  else unlockTTS();
  updateTTSButton();
}

function updateTTSButton() {
  const btn = document.getElementById("btn-tts");
  if (!btn) return;
  btn.classList.toggle("active", ttsEnabled);
  btn.classList.toggle("muted",  !ttsEnabled);
  btn.title = ttsEnabled ? "Lecture vocale activée" : "Lecture vocale désactivée";
}

// ── Microphone (push-to-talk) ──

async function requestMicPermission() {
  try { await navigator.mediaDevices.getUserMedia({ audio: true }); }
  catch (e) { addSystemMessage("⚠️ Accès au microphone refusé."); }
}

async function startRecording() {
  if (vadActive) return; // VAD prioritaire
  if (mediaRecorder && mediaRecorder.state === "recording") return;

  let stream;
  try { stream = await navigator.mediaDevices.getUserMedia({ audio: true }); }
  catch (e) { addSystemMessage("⚠️ Impossible d'accéder au microphone."); return; }

  audioChunks = [];
  const mimeType = MediaRecorder.isTypeSupported("audio/webm;codecs=opus")
    ? "audio/webm;codecs=opus" : "audio/mp4";

  mediaRecorder = new MediaRecorder(stream, { mimeType });
  mediaRecorder.ondataavailable = (e) => { if (e.data.size > 0) audioChunks.push(e.data); };
  mediaRecorder.onstop = () => { stream.getTracks().forEach(t => t.stop()); sendAudio(); };
  mediaRecorder.start();

  document.getElementById("btn-mic").classList.add("recording");
  document.getElementById("recording-indicator").classList.remove("hidden");
}

function stopRecording() {
  if (vadActive) return;
  if (!mediaRecorder || mediaRecorder.state !== "recording") return;
  mediaRecorder.stop();
  document.getElementById("btn-mic").classList.remove("recording");
  document.getElementById("recording-indicator").classList.add("hidden");
}

// ── VAD ──

async function toggleVAD() {
  if (vadActive) stopVAD();
  else await startVAD();
}

async function startVAD() {
  try { vadStream = await navigator.mediaDevices.getUserMedia({ audio: true }); }
  catch (e) { addSystemMessage("⚠️ Impossible d'accéder au microphone."); return; }

  unlockTTS();

  vadAudioCtx  = new AudioContext();
  vadAnalyser  = vadAudioCtx.createAnalyser();
  vadAnalyser.fftSize = 512;
  vadAudioCtx.createMediaStreamSource(vadStream).connect(vadAnalyser);

  vadActive    = true;
  vadDetecting = true;

  document.getElementById("btn-mic").disabled = true;
  document.getElementById("vad-listening").classList.remove("hidden");

  updateVADButton();
  addSystemMessage("🎙️ Mode auto activé — parle naturellement");
  requestAnimationFrame(detectVoice);
}

function stopVAD() {
  vadDetecting = false;
  vadActive    = false;
  vadSpeaking  = false;
  clearTimeout(vadSilenceTimer);
  clearTimeout(vadMaxTimer);

  if (mediaRecorder && mediaRecorder.state === "recording") mediaRecorder.stop();
  if (vadAudioCtx) { vadAudioCtx.close(); vadAudioCtx = null; }
  if (vadStream)   { vadStream.getTracks().forEach(t => t.stop()); vadStream = null; }

  document.getElementById("btn-mic").disabled = false;
  document.getElementById("vad-listening").classList.add("hidden");
  document.getElementById("recording-indicator").classList.add("hidden");

  updateVADButton();
  addSystemMessage("🎙️ Mode auto désactivé");
}

function getVolume() {
  const data = new Uint8Array(vadAnalyser.frequencyBinCount);
  vadAnalyser.getByteFrequencyData(data);
  return data.reduce((a, b) => a + b, 0) / data.length;
}

function detectVoice() {
  if (!vadDetecting) return;

  if (getVolume() > VAD_THRESHOLD) {
    clearTimeout(vadSilenceTimer);

    if (!vadSpeaking) {
      vadSpeaking = true;
      startVADRecording();
    }

    vadSilenceTimer = setTimeout(() => {
      vadSpeaking = false;
      stopVADRecording();
    }, VAD_SILENCE_DELAY);
  }

  requestAnimationFrame(detectVoice);
}

function startVADRecording() {
  if (mediaRecorder && mediaRecorder.state === "recording") return;

  audioChunks = [];
  const mimeType = MediaRecorder.isTypeSupported("audio/webm;codecs=opus")
    ? "audio/webm;codecs=opus" : "audio/mp4";

  mediaRecorder = new MediaRecorder(vadStream, { mimeType });
  mediaRecorder.ondataavailable = (e) => { if (e.data.size > 0) audioChunks.push(e.data); };
  mediaRecorder.onstop = sendAudio;
  mediaRecorder.start();

  document.getElementById("recording-indicator").classList.remove("hidden");

  vadMaxTimer = setTimeout(() => {
    if (vadSpeaking) { vadSpeaking = false; stopVADRecording(); }
  }, VAD_MAX_DURATION);
}

function stopVADRecording() {
  clearTimeout(vadMaxTimer);
  if (mediaRecorder && mediaRecorder.state === "recording") mediaRecorder.stop();
  document.getElementById("recording-indicator").classList.add("hidden");
}

function updateVADButton() {
  const btn = document.getElementById("btn-vad");
  if (!btn) return;
  btn.classList.toggle("active", vadActive);
  btn.title = vadActive ? "Mode auto activé (cliquer pour désactiver)" : "Activer la détection automatique";
}

// ── Envoi audio ──

function sendAudio() {
  if (!audioChunks.length) return;
  if (!ws || ws.readyState !== WebSocket.OPEN) {
    addSystemMessage("⚠️ Non connecté au serveur.");
    return;
  }
  const blob   = new Blob(audioChunks, { type: audioChunks[0].type });
  const reader = new FileReader();
  reader.onloadend = () => {
    const base64 = reader.result.split(",")[1];
    ws.send(JSON.stringify({ type: "audio", data: base64, lang: userLang }));
    addSystemMessage("⏳ Transcription en cours…");
  };
  reader.readAsDataURL(blob);
  audioChunks = [];
}
