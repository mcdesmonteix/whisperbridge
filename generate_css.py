css_content = """/* ── Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  /* Default to Aurora if nothing is set */
  --bg: #080c14;
  --surface: rgba(255,255,255,0.04);
  --surface2: rgba(255,255,255,0.07);
  --border: rgba(255,255,255,0.08);
  --text: #f0f6ff;
  --text-muted: rgba(180,210,255,0.55);
  --text-dim: rgba(180,210,255,0.3);
  --accent: #a78bfa;
  --gradient: linear-gradient(135deg, #2dd4bf, #818cf8, #c084fc);
  --gradient-btn: linear-gradient(135deg, #0ea5e9, #6366f1, #a855f7);
  --me-bubble: linear-gradient(135deg, #0d9488, #4f46e5);
  --other-bubble: rgba(255,255,255,0.06);
  --online: #34d399;
  --scrollbar: rgba(255,255,255,0.08);
  --font: 'Inter', -apple-system, sans-serif;
}

[data-theme="aurora"] {
  --bg: #080c14;
  --surface: rgba(255,255,255,0.04);
  --surface2: rgba(255,255,255,0.07);
  --border: rgba(255,255,255,0.08);
  --text: #f0f6ff;
  --text-muted: rgba(180,210,255,0.55);
  --text-dim: rgba(180,210,255,0.3);
  --accent: #a78bfa;
  --gradient: linear-gradient(135deg, #2dd4bf, #818cf8, #c084fc);
  --gradient-btn: linear-gradient(135deg, #0ea5e9, #6366f1, #a855f7);
  --me-bubble: linear-gradient(135deg, #0d9488, #4f46e5);
  --other-bubble: rgba(255,255,255,0.06);
  --online: #34d399;
  --scrollbar: rgba(255,255,255,0.08);
  --font: 'Inter', -apple-system, sans-serif;
}

[data-theme="linear"] {
  --bg: #f5f5f7;
  --surface: #ffffff;
  --surface2: #f0f0f2;
  --border: #e4e4e8;
  --border-strong: #d0d0d8;
  --text: #111118;
  --text-muted: #6b6b80;
  --text-dim: #9b9baa;
  --accent: #4f46e5;
  --accent-light: rgba(79,70,229,0.08);
  --me-bubble: #4f46e5;
  --other-bubble: #ffffff;
  --online: #22c55e;
  --scrollbar: #e0e0e8;
  --font: 'Inter', -apple-system, sans-serif;
  --shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 16px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 24px rgba(0,0,0,0.08), 0 1px 4px rgba(0,0,0,0.04);
}

[data-theme="neon"] {
  --bg: #0c0c14;
  --surface: rgba(255,255,255,0.03);
  --surface2: rgba(255,255,255,0.06);
  --border: rgba(255,255,255,0.07);
  --text: #f5f0ff;
  --text-muted: rgba(200,180,255,0.6);
  --text-dim: rgba(200,180,255,0.3);
  --accent: #ff4da6;
  --gradient: linear-gradient(135deg, #ff6b6b, #ff4da6, #9b59ff);
  --gradient-btn: linear-gradient(135deg, #ff6b6b, #ff4da6, #9b59ff);
  --me-bubble: linear-gradient(135deg, #ff4da6, #9b59ff);
  --other-bubble: rgba(255,255,255,0.05);
  --online: #00ffb3;
  --scrollbar: rgba(155,89,255,0.2);
  --font: 'Outfit', -apple-system, sans-serif;
}

body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  height: 100dvh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: background 0.3s, color 0.3s;
}

.hidden { display: none !important; }

/* ── THEME SELECTOR ── */
.theme-picker { display: flex; gap: 8px; align-items: center; justify-content: center; }
.theme-picker-label { font-size: 0.72rem; color: var(--text-muted); margin-bottom: 8px; margin-top: 20px; text-transform: uppercase; font-weight: 600; letter-spacing: 0.05em; text-align:center; }
.theme-swatch {
  width: 26px; height: 26px; border-radius: 50%; cursor: pointer;
  border: 2px solid transparent; transition: all 0.15s; position: relative;
}
.theme-swatch:hover { transform: scale(1.15); }
.theme-swatch.active { border-color: var(--text); box-shadow: 0 0 0 2px rgba(0,0,0,0.2); }
.theme-swatch[data-theme="aurora"] { background: linear-gradient(135deg, #0ea5e9, #a855f7); }
.theme-swatch[data-theme="linear"] { background: #4f46e5; }
.theme-swatch[data-theme="neon"]   { background: linear-gradient(135deg, #ff6b6b, #9b59ff); }
.theme-swatch::after {
  content: attr(data-label); position: absolute; bottom: -22px; left: 50%;
  transform: translateX(-50%); font-size: 0.6rem; white-space: nowrap;
  color: var(--text-muted); opacity: 0; transition: opacity 0.15s; pointer-events: none;
}
.theme-swatch:hover::after { opacity: 1; }

.theme-dropdown {
  position: absolute; top: 40px; right: 0;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 14px; padding: 10px; display: flex; gap: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2); z-index: 100;
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
}

/* ── AURORA BG ── */
.aurora-bg { position: fixed; inset: 0; z-index: 0; overflow: hidden; pointer-events: none; display: none; }
[data-theme="aurora"] .aurora-bg { display: block; }
.aurora-bg::before {
  content: ''; position: absolute; top: -40%; left: -20%; width: 80%; height: 80%;
  background: radial-gradient(ellipse, rgba(56,189,248,0.18) 0%, transparent 70%);
  animation: drift1 12s ease-in-out infinite alternate;
}
.aurora-bg::after {
  content: ''; position: absolute; top: -20%; right: -20%; width: 70%; height: 70%;
  background: radial-gradient(ellipse, rgba(168,85,247,0.15) 0%, transparent 70%);
  animation: drift2 15s ease-in-out infinite alternate;
}
.aurora-spot {
  position: absolute; bottom: 10%; left: 10%; width: 50%; height: 40%;
  background: radial-gradient(ellipse, rgba(45,212,191,0.1) 0%, transparent 70%);
  animation: drift1 18s ease-in-out infinite alternate-reverse;
}
@keyframes drift1 { from { transform: translate(0,0) scale(1); } to { transform: translate(60px,40px) scale(1.1); } }
@keyframes drift2 { from { transform: translate(0,0) scale(1); } to { transform: translate(-50px,60px) scale(0.9); } }

/* ── NEON BG ── */
.wave-bg, .glow-spot { display: none; }
[data-theme="neon"] .wave-bg, [data-theme="neon"] .glow-spot { display: block; }
.wave-bg { position: fixed; bottom: 0; left: 0; right: 0; height: 280px; z-index: 0; pointer-events: none; overflow: hidden; }
.wave { position: absolute; bottom: 0; width: 200%; height: 100%; background: linear-gradient(0deg, rgba(155,89,255,0.06) 0%, transparent 100%); }
.wave::before {
  content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 120px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 120'%3E%3Cpath fill='rgba(155,89,255,0.08)' d='M0,60L48,50C96,40,192,20,288,26.7C384,33,480,67,576,73.3C672,80,768,60,864,46.7C960,33,1056,27,1152,33.3C1248,40,1344,60,1392,70L1440,80L1440,120L0,120Z'/%3E%3C/svg%3E") repeat-x bottom;
  animation: wave-move 8s linear infinite;
}
.wave::after {
  content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 80px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 80'%3E%3Cpath fill='rgba(255,77,166,0.06)' d='M0,40L60,45C120,50,240,60,360,58.7C480,57,600,43,720,37.3C840,31,960,33,1080,38.7C1200,44,1320,54,1380,58.7L1440,63L1440,80L0,80Z'/%3E%3C/svg%3E") repeat-x bottom;
  animation: wave-move 12s linear infinite reverse;
}
@keyframes wave-move { from{background-position-x:0} to{background-position-x:1440px} }
.glow-spot { position: fixed; border-radius: 50%; filter: blur(100px); opacity: 0.12; pointer-events: none; z-index: 0; }
.glow-spot.g1 { width: 500px; height: 500px; background: #9b59ff; top: -200px; right: -100px; }
.glow-spot.g2 { width: 400px; height: 400px; background: #ff4da6; bottom: -150px; left: -100px; }

/* ── LINEAR BG ── */
[data-theme="linear"] body::before {
  content: ''; position: absolute; inset: 0; pointer-events: none; z-index:0;
  background:
    radial-gradient(600px 400px at 20% 80%, rgba(79,70,229,0.04) 0%, transparent 100%),
    radial-gradient(400px 300px at 80% 20%, rgba(139,92,246,0.04) 0%, transparent 100%);
}

/* ── LOGIN SCREEN ── */
#screen-select { position: relative; z-index: 1; display: flex; align-items: center; justify-content: center; height: 100dvh; }
.select-card {
  background: var(--surface); border: 1px solid var(--border);
  padding: 48px 40px 40px; width: 380px; text-align: center;
  position: relative; z-index: 1;
}

[data-theme="aurora"] .select-card { border-radius: 28px; backdrop-filter: blur(32px); -webkit-backdrop-filter: blur(32px); box-shadow: 0 0 0 1px rgba(56,189,248,0.06), 0 32px 64px rgba(0,0,0,0.5); }
[data-theme="linear"] .select-card { border-radius: 20px; box-shadow: var(--shadow-md); }
[data-theme="neon"] .select-card { border-radius: 28px; backdrop-filter: blur(40px); -webkit-backdrop-filter: blur(40px); box-shadow: 0 0 0 1px rgba(255,77,166,0.05), 0 32px 80px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.06); border-color: rgba(155,89,255,0.2); }

.logo-wrap { display: flex; flex-direction: column; align-items: center; margin-bottom: 28px; gap: 8px; }
[data-theme="aurora"] .logo-wrap { flex-direction: column; }

.logo-icon { display: flex; align-items: center; justify-content: center; }
[data-theme="aurora"] .logo-icon { width: 64px; height: 64px; border-radius: 18px; background: linear-gradient(135deg, #0d9488, #4f46e5); font-size: 28px; box-shadow: 0 0 32px rgba(56,189,248,0.3), 0 8px 24px rgba(0,0,0,0.4); margin-bottom: 16px;}
[data-theme="linear"] .logo-icon { width: 52px; height: 52px; border-radius: 14px; background: var(--accent); font-size: 24px; box-shadow: 0 4px 16px rgba(79,70,229,0.3); }
[data-theme="neon"] .logo-icon { width: 72px; height: 72px; border-radius: 22px; background: var(--gradient); font-size: 32px; box-shadow: 0 0 40px rgba(155,89,255,0.5), 0 8px 24px rgba(0,0,0,0.4); margin-bottom: 8px; position: relative; }
[data-theme="neon"] .logo-icon::before { content: ''; position: absolute; inset: -3px; border-radius: 24px; background: var(--gradient); z-index: -1; filter: blur(12px); opacity: 0.6; }

.app-title { font-weight: 800; }
[data-theme="aurora"] .app-title { font-size: 1.9rem; letter-spacing: -0.5px; background: linear-gradient(135deg, #e0f2fe, #c4b5fd); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
[data-theme="linear"] .app-title { font-size: 1.5rem; color: var(--text); letter-spacing: -0.4px; }
[data-theme="neon"] .app-title { font-size: 2rem; letter-spacing: -0.5px; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

.app-subtitle { font-size: 0.83rem; color: var(--text-muted); text-align: center; font-weight: 400; }

.label { font-size: 0.78rem; font-weight: 600; color: var(--text-muted); margin-bottom: 7px; display: block; text-align: left;}
[data-theme="aurora"] .label { font-size: 0.73rem; text-transform: uppercase; letter-spacing: 0.06em; }
[data-theme="neon"] .label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.07em; }

.form-group { margin-bottom: 14px; text-align: left; }
.form-group input, .form-group select {
  width: 100%; padding: 13px 16px; background: var(--surface); border: 1px solid var(--border);
  color: var(--text); outline: none; font-family: var(--font); transition: border-color 0.2s, box-shadow 0.2s;
}
.form-group input::placeholder { color: var(--text-dim); }
.form-group select option { background: #111118; color: #fff; }
[data-theme="linear"] .form-group select option { background: #fff; color: #111; }

[data-theme="aurora"] .form-group input, [data-theme="aurora"] .form-group select { border-radius: 14px; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1); }
[data-theme="linear"] .form-group input, [data-theme="linear"] .form-group select { border-radius: 10px; padding: 11px 14px; border-width: 1.5px; }
[data-theme="neon"] .form-group input, [data-theme="neon"] .form-group select { border-radius: 14px; background: rgba(255,255,255,0.04); border-color: rgba(255,255,255,0.08); }

.form-group input:focus, .form-group select:focus {
  border-color: var(--accent); box-shadow: 0 0 0 3px rgba(124,111,255,0.15);
}
[data-theme="aurora"] .form-group input:focus, [data-theme="aurora"] .form-group select:focus { border-color: rgba(56,189,248,0.5); box-shadow: 0 0 0 3px rgba(56,189,248,0.08); }
[data-theme="linear"] .form-group input:focus, [data-theme="linear"] .form-group select:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(79,70,229,0.1); }
[data-theme="neon"] .form-group input:focus, [data-theme="neon"] .form-group select:focus { border-color: rgba(155,89,255,0.5); box-shadow: 0 0 0 3px rgba(155,89,255,0.08), 0 0 16px rgba(155,89,255,0.12); }

.btn-join {
  width: 100%; border: none; color: #fff; font-weight: 700; cursor: pointer;
  margin-top: 6px; font-family: var(--font); transition: all 0.15s; position: relative; overflow: hidden;
}
[data-theme="aurora"] .btn-join { padding: 14px; background: var(--gradient-btn); border-radius: 14px; font-size: 0.95rem; letter-spacing: 0.02em; box-shadow: 0 4px 20px rgba(99,102,241,0.35); }
[data-theme="aurora"] .btn-join::after { content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(255,255,255,0.15), transparent); pointer-events: none; }
[data-theme="aurora"] .btn-join:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(99,102,241,0.45); }

[data-theme="linear"] .btn-join { padding: 13px; background: var(--accent); border-radius: 10px; font-size: 0.92rem; font-weight: 600; box-shadow: 0 2px 8px rgba(79,70,229,0.3); }
[data-theme="linear"] .btn-join:hover { background: #4338ca; transform: translateY(-1px); box-shadow: 0 4px 16px rgba(79,70,229,0.35); }

[data-theme="neon"] .btn-join { padding: 15px; background: var(--gradient); border-radius: 14px; font-size: 1rem; letter-spacing: 0.03em; box-shadow: 0 6px 24px rgba(155,89,255,0.4), 0 2px 8px rgba(255,77,166,0.3); }
[data-theme="neon"] .btn-join::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(255,255,255,0.12) 0%, transparent 100%); }
[data-theme="neon"] .btn-join:hover { transform: translateY(-2px); box-shadow: 0 10px 30px rgba(155,89,255,0.5); }


.help-text { font-size: 0.72rem; color: var(--text-dim); text-align: center; margin-top: 18px; line-height: 1.6; }
[data-theme="neon"] .pill-hint {
  display: inline-flex; align-items: center; gap: 6px; margin-top: 22px; background: rgba(155,89,255,0.08);
  border: 1px solid rgba(155,89,255,0.15); border-radius: 20px; padding: 5px 14px; font-size: 0.7rem; color: rgba(200,180,255,0.7);
}

/* ── CHAT SCREEN ── */
#screen-chat { position: relative; z-index: 1; display: flex; flex-direction: column; height: 100dvh; }

header {
  background: var(--surface); padding: 0 20px;
  display: flex; align-items: center; justify-content: space-between; flex-shrink: 0;
  border-bottom: 1px solid var(--border);
}
[data-theme="aurora"] header { background: rgba(8,12,20,0.7); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); height: 60px; }
[data-theme="linear"] header { height: 56px; }
[data-theme="neon"] header { background: rgba(12,12,20,0.8); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); height: 58px; border-color: rgba(155,89,255,0.15); }

.header-left { display: flex; align-items: center; gap: 12px; }
[data-theme="linear"] .header-left { gap: 10px; }

.header-logo { display: flex; align-items: center; justify-content: center; }
[data-theme="aurora"] .header-logo { width: 32px; height: 32px; border-radius: 10px; background: var(--gradient-btn); font-size: 15px; box-shadow: 0 0 14px rgba(99,102,241,0.4); }
[data-theme="linear"] .header-logo { width: 28px; height: 28px; border-radius: 8px; background: var(--accent); font-size: 13px; }
[data-theme="neon"] .header-logo { width: 30px; height: 30px; border-radius: 9px; background: var(--gradient); font-size: 14px; box-shadow: 0 0 12px rgba(155,89,255,0.4); }

.header-title { font-weight: 700; font-size: 0.95rem; color: var(--text); }
[data-theme="linear"] .header-title { font-size: 0.92rem; }

.header-sep { color: var(--border-strong); font-size: 0.9rem; }
[data-theme="aurora"] .header-sep { display: none; }
[data-theme="neon"] .header-sep { display: none; }

.header-room { font-size: 0.72rem; color: var(--text-muted); }
[data-theme="aurora"] .header-room { background: rgba(255,255,255,0.05); border: 1px solid var(--border); border-radius: 6px; padding: 2px 8px; }
[data-theme="linear"] .header-room { font-weight: 500; }
[data-theme="neon"] .header-room { background: rgba(155,89,255,0.08); border: 1px solid rgba(155,89,255,0.15); border-radius: 6px; padding: 2px 8px; }

.header-right { display: flex; align-items: center; gap: 8px; }
[data-theme="linear"] .header-right { gap: 6px; }

.user-pill {
  display: flex; align-items: center; gap: 6px; padding: 5px 12px;
  border-radius: 20px; font-size: 0.75rem; font-weight: 600;
  background: var(--surface2); border: 1px solid var(--border); color: var(--text-muted);
}
[data-theme="aurora"] .user-pill { background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1); }
[data-theme="linear"] .user-pill { padding: 4px 10px; font-size: 0.73rem; }
[data-theme="neon"] .user-pill { padding: 4px 10px; font-size: 0.73rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.08); }

.user-pill.me { background: var(--accent-light); border-color: rgba(79,70,229,0.2); color: var(--accent); }
[data-theme="aurora"] .user-pill.me { background: rgba(99,102,241,0.12); border-color: rgba(99,102,241,0.3); color: #a5b4fc; }
[data-theme="neon"] .user-pill.me { background: rgba(155,89,255,0.1); border-color: rgba(155,89,255,0.25); color: #c4a7ff; }

.user-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--online); box-shadow: 0 0 6px var(--online); }
[data-theme="aurora"] .user-dot { animation: pulse-dot 2s ease-in-out infinite; }
[data-theme="linear"] .user-dot { width: 6px; height: 6px; box-shadow: none; }
[data-theme="neon"] .user-dot { width: 6px; height: 6px; }
@keyframes pulse-dot { 0%,100%{opacity:1} 50%{opacity:0.5} }

.btn-icon {
  width: 34px; height: 34px; border-radius: 10px; background: var(--surface2); border: 1px solid var(--border);
  color: var(--text-muted); font-size: 0.85rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.15s;
}
[data-theme="aurora"] .btn-icon { background: rgba(255,255,255,0.05); }
[data-theme="aurora"] .btn-icon:hover { background: rgba(255,255,255,0.08); color: var(--text); }
[data-theme="linear"] .btn-icon { width: 32px; height: 32px; border-radius: 8px; font-size: 0.82rem; }
[data-theme="linear"] .btn-icon:hover { background: var(--border); color: var(--text); }
[data-theme="neon"] .btn-icon { width: 32px; height: 32px; border-radius: 9px; background: rgba(255,255,255,0.04); font-size: 0.82rem; }
[data-theme="neon"] .btn-icon:hover { border-color: rgba(155,89,255,0.3); color: #c4a7ff; }

/* ── MESSAGES ── */
#messages { flex: 1; overflow-y: auto; padding: 20px 20px 10px; display: flex; flex-direction: column; gap: 12px; }
[data-theme="linear"] #messages { gap: 10px; }
#messages::-webkit-scrollbar { width: 3px; }
[data-theme="linear"] #messages::-webkit-scrollbar { width: 4px; }
#messages::-webkit-scrollbar-thumb { background: var(--scrollbar); border-radius: 3px; }

.msg-system { text-align: center; font-size: 0.71rem; color: var(--text-dim); padding: 2px 0; }
[data-theme="linear"] .msg-system { font-size: 0.68rem; }
[data-theme="neon"] .msg-system { font-size: 0.68rem; }
[data-theme="neon"] .msg-system span { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 20px; padding: 3px 12px; display: inline-block; }

.message { max-width: 72%; display: flex; flex-direction: column; gap: 4px; }
[data-theme="linear"] .message { max-width: 70%; gap: 3px; }
.message.me { align-self: flex-end; align-items: flex-end; }
.message.other { align-self: flex-start; align-items: flex-start; }

.message-sender { font-size: 0.68rem; color: var(--text-muted); padding: 0 6px; font-weight: 500; }
[data-theme="linear"] .message-sender { font-size: 0.67rem; color: var(--text-dim); }

.message-bubble { padding: 11px 16px; border-radius: 18px; font-size: 0.9rem; line-height: 1.55; }
[data-theme="linear"] .message-bubble { padding: 10px 14px; border-radius: 16px; line-height: 1.5; }

.message.me .message-bubble { background: var(--me-bubble); color: #fff; border-bottom-right-radius: 6px; }
[data-theme="aurora"] .message.me .message-bubble { box-shadow: 0 4px 16px rgba(79,70,229,0.25); }
[data-theme="linear"] .message.me .message-bubble { border-bottom-right-radius: 5px; }
[data-theme="neon"] .message.me .message-bubble { border-bottom-right-radius: 5px; box-shadow: 0 4px 20px rgba(155,89,255,0.3); }

.message.other .message-bubble { background: var(--other-bubble); color: var(--text); border: 1px solid var(--border); border-bottom-left-radius: 6px; }
[data-theme="linear"] .message.other .message-bubble { border-bottom-left-radius: 5px; box-shadow: var(--shadow); }
[data-theme="neon"] .message.other .message-bubble { border-bottom-left-radius: 5px; }

.message-translation { font-size: 0.73rem; color: var(--text-muted); font-style: italic; padding: 0 6px; }
[data-theme="linear"] .message-translation { font-size: 0.71rem; color: var(--text-dim); }
[data-theme="neon"] .message-translation { font-size: 0.72rem; color: rgba(200,180,255,0.5); }
.message-meta { font-size: 0.65rem; color: var(--text-dim); padding: 0 6px; }
[data-theme="linear"] .message-meta { font-size: 0.63rem; }
[data-theme="neon"] .message-meta { font-size: 0.63rem; }

/* ── SHARE PROMPT ── */
.msg-share-prompt {
  background: rgba(99,102,241,0.06); border: 1px solid rgba(99,102,241,0.2);
  border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 8px;
  align-self: center; max-width: 90%; text-align: center;
}
[data-theme="linear"] .msg-share-prompt { background: var(--accent-light); border: 1.5px solid rgba(79,70,229,0.2); border-radius: 14px; max-width: 88%; }
[data-theme="neon"] .msg-share-prompt { background: rgba(155,89,255,0.06); border: 1px solid rgba(155,89,255,0.2); max-width: 88%; }

.msg-share-title { font-size: 0.9rem; font-weight: 700; color: var(--text); }
.msg-share-subtitle { font-size: 0.77rem; color: var(--text-muted); }
.msg-share-url {
  font-size: 0.72rem; font-family: monospace; background: rgba(255,255,255,0.05);
  border: 1px solid var(--border); border-radius: 8px; padding: 7px 10px; word-break: break-all; color: var(--text-muted);
}
[data-theme="linear"] .msg-share-url { background: var(--surface); border-radius: 7px; }
[data-theme="neon"] .msg-share-url { background: rgba(255,255,255,0.04); }

.msg-share-btn {
  background: var(--gradient-btn); color: #fff; border: none; border-radius: 10px; padding: 9px;
  font-size: 0.82rem; font-weight: 600; cursor: pointer; font-family: var(--font); transition: opacity 0.15s;
}
[data-theme="linear"] .msg-share-btn { background: var(--accent); border-radius: 8px; }
[data-theme="neon"] .msg-share-btn { background: var(--gradient); }
.msg-share-btn:hover { opacity: 0.85; }
[data-theme="linear"] .msg-share-btn:hover { opacity: 0.9; }

/* ── FOOTER ── */
footer {
  background: var(--surface); border-top: 1px solid var(--border);
  padding: 14px 24px 24px; display: flex; flex-direction: column; align-items: center; gap: 12px; flex-shrink: 0;
}
[data-theme="aurora"] footer { background: rgba(8,12,20,0.7); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); }
[data-theme="neon"] footer { background: rgba(12,12,20,0.8); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-color: rgba(155,89,255,0.12); padding-bottom: 28px; }

.status-indicator { font-size: 0.78rem; font-weight: 600; display: flex; align-items: center; gap: 6px; }
[data-theme="linear"] .status-indicator { font-size: 0.77rem; }
.status-indicator .dot { width: 6px; height: 6px; border-radius: 50%; }
[data-theme="neon"] .status-indicator .dot { width: 7px; height: 7px; }

.status-indicator.recording { color: #f87171; }
.status-indicator.recording .dot { background: #ef4444; box-shadow: 0 0 6px #ef4444; animation: pulse-dot 0.8s infinite; }
[data-theme="linear"] .status-indicator.recording { color: #ef4444; }
[data-theme="linear"] .status-indicator.recording .dot { box-shadow: none; animation: blink 0.8s infinite; }
[data-theme="neon"] .status-indicator.recording { color: #ff6b6b; }
[data-theme="neon"] .status-indicator.recording .dot { background: #ff6b6b; box-shadow: 0 0 8px #ff6b6b; animation: blink 0.8s infinite; }

.status-indicator.listening { color: #34d399; }
.status-indicator.listening .dot { background: #34d399; box-shadow: 0 0 6px #34d399; animation: pulse-dot 2s infinite; }
[data-theme="linear"] .status-indicator.listening { color: #22c55e; }
[data-theme="linear"] .status-indicator.listening .dot { background: #22c55e; box-shadow: none; animation: blink 2s infinite; }
[data-theme="neon"] .status-indicator.listening { color: var(--online); }
[data-theme="neon"] .status-indicator.listening .dot { background: var(--online); box-shadow: 0 0 8px var(--online); animation: blink 2s infinite; }

.status-indicator.paused { color: #fbbf24; }
[data-theme="linear"] .status-indicator.paused { color: #f59e0b; }
[data-theme="neon"] .status-indicator.paused { color: #ffb347; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }

.footer-controls { display: flex; align-items: center; gap: 16px; }
[data-theme="linear"] .footer-controls { gap: 12px; }

#btn-mic {
  width: 68px; height: 68px; border-radius: 50%; border: none; background: var(--gradient-btn);
  font-size: 1.6rem; cursor: pointer; transition: all 0.15s; display: flex; align-items: center; justify-content: center; position: relative;
}
[data-theme="aurora"] #btn-mic { box-shadow: 0 0 0 0 rgba(99,102,241,0), 0 6px 20px rgba(99,102,241,0.4); }
[data-theme="aurora"] #btn-mic::before { content: ''; position: absolute; inset: -4px; border-radius: 50%; border: 2px solid rgba(99,102,241,0.25); animation: ring-pulse 2.5s ease-in-out infinite; }
@keyframes ring-pulse { 0%,100%{opacity:0.4;transform:scale(1)} 50%{opacity:0.1;transform:scale(1.08)} }

[data-theme="linear"] #btn-mic { width: 64px; height: 64px; background: var(--accent); font-size: 1.55rem; box-shadow: 0 4px 16px rgba(79,70,229,0.35); }

[data-theme="neon"] #btn-mic { width: 72px; height: 72px; background: var(--gradient); font-size: 1.7rem; box-shadow: 0 0 30px rgba(155,89,255,0.4), 0 6px 24px rgba(0,0,0,0.3); }
[data-theme="neon"] #btn-mic::before { content: ''; position: absolute; inset: -6px; border-radius: 50%; border: 2px solid rgba(155,89,255,0.3); animation: ring-expand 2.5s ease-in-out infinite; }
[data-theme="neon"] #btn-mic::after { content: ''; position: absolute; inset: -12px; border-radius: 50%; border: 1.5px solid rgba(155,89,255,0.12); animation: ring-expand 2.5s 0.8s ease-in-out infinite; }
@keyframes ring-expand { 0%,100%{opacity:0.5;transform:scale(1)} 50%{opacity:0.1;transform:scale(1.1)} }

#btn-mic:active, #btn-mic.recording { transform: scale(0.95); }
[data-theme="aurora"] #btn-mic:active, [data-theme="aurora"] #btn-mic.recording { background: linear-gradient(135deg,#ef4444,#f97316) !important; box-shadow: 0 6px 24px rgba(239,68,68,0.45) !important; }
[data-theme="linear"] #btn-mic:active, [data-theme="linear"] #btn-mic.recording { background: #ef4444 !important; box-shadow: 0 4px 16px rgba(239,68,68,0.4) !important; }
[data-theme="neon"] #btn-mic:active, [data-theme="neon"] #btn-mic.recording { background: linear-gradient(135deg,#ef4444,#ff6b6b) !important; box-shadow: 0 0 30px rgba(239,68,68,0.5) !important; transform: scale(0.94); }

.btn-sm {
  width: 48px; height: 48px; border-radius: 14px; background: var(--surface2); border: 1px solid var(--border);
  color: var(--text-muted); font-size: 1.15rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.15s; position: relative;
}
[data-theme="aurora"] .btn-sm { background: rgba(255,255,255,0.05); }
[data-theme="aurora"] .btn-sm:hover { background: rgba(255,255,255,0.08); color: var(--text); }
[data-theme="linear"] .btn-sm { width: 46px; height: 46px; border-radius: 12px; border-width: 1.5px; font-size: 1.1rem; }
[data-theme="linear"] .btn-sm:hover { background: var(--border); color: var(--text); }
[data-theme="neon"] .btn-sm { width: 50px; height: 50px; border-radius: 50%; background: rgba(255,255,255,0.04); font-size: 1.2rem; }
[data-theme="neon"] .btn-sm:hover { border-color: rgba(155,89,255,0.3); color: #c4a7ff; }

.btn-sm.active { box-shadow: 0 0 0 3px rgba(45,212,191,0.08); }
[data-theme="aurora"] .btn-sm.active { background: rgba(45,212,191,0.1); border-color: rgba(45,212,191,0.4); color: #2dd4bf; }
[data-theme="linear"] .btn-sm.active { background: rgba(34,197,94,0.08); border-color: rgba(34,197,94,0.35); color: #16a34a; box-shadow: none; }
[data-theme="neon"] .btn-sm.active { background: rgba(0,255,179,0.08); border-color: rgba(0,255,179,0.3); color: var(--online); box-shadow: 0 0 12px rgba(0,255,179,0.15); }

[data-theme="aurora"] .btn-sm.active.pause { background: rgba(251,191,36,0.1); border-color: rgba(251,191,36,0.4); color: #fbbf24; }
[data-theme="linear"] .btn-sm.active.pause { background: rgba(245,158,11,0.08); border-color: rgba(245,158,11,0.35); color: #d97706; }
[data-theme="neon"] .btn-sm.active.pause { background: rgba(255,179,71,0.08); border-color: rgba(255,179,71,0.3); color: #ffb347; }

.btn-sm.muted { opacity: 0.35; }
[data-theme="neon"] .btn-sm.muted { opacity: 0.3; }

.footer-hint { font-size: 0.68rem; color: var(--text-dim); display: flex; align-items: center; gap: 4px; }
[data-theme="aurora"] .footer-hint .sep { opacity: 0.3; }
[data-theme="linear"] .footer-hint { font-size: 0.67rem; }
[data-theme="neon"] .footer-hint { font-size: 0.67rem; }

#btn-share {
  font-size: 0.72rem; color: var(--text-muted); background: var(--surface2); border: 1px solid var(--border);
  border-radius: 20px; padding: 5px 14px; cursor: pointer; font-family: var(--font); transition: all 0.15s;
}
[data-theme="aurora"] #btn-share { background: rgba(255,255,255,0.04); }
[data-theme="aurora"] #btn-share:hover { color: var(--text); border-color: rgba(56,189,248,0.3); }
[data-theme="linear"] #btn-share:hover { color: var(--accent); border-color: rgba(79,70,229,0.3); }
[data-theme="neon"] #btn-share { background: rgba(155,89,255,0.06); border-color: rgba(155,89,255,0.15); }
[data-theme="neon"] #btn-share:hover { color: #c4a7ff; border-color: rgba(155,89,255,0.35); }
"""

with open("/Users/mcdesmonteix/Developer/projet_olivia_v2_antigravity/static/style.css", "w") as f:
    f.write(css_content)
