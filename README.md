# 💬 Projet Olivia

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-green?logo=fastapi)
![Whisper](https://img.shields.io/badge/Whisper-small-orange?logo=openai)
![LibreTranslate](https://img.shields.io/badge/LibreTranslate-1.9-purple)
![Langues](https://img.shields.io/badge/Langues-FR%20%E2%86%94%20EN-red)
![100% Local](https://img.shields.io/badge/100%25-Local-darkgreen)
![Licence MIT](https://img.shields.io/badge/Licence-MIT-yellow)
![POC Validé](https://img.shields.io/badge/POC-Validé%20✅-brightgreen)

Application de conversation bilingue en temps réel, permettant à deux personnes de se parler malgré la barrière de la langue.

**Exemple d'usage :** Louise (🇫🇷 français) et Olivia (🇺🇸 anglais) peuvent se parler naturellement — chacune parle dans sa langue, l'autre voit la traduction instantanément.

## 🎬 Démonstration

<video src="docs/media/demo.mov" controls width="100%"></video>

> Si la vidéo ne s'affiche pas, [cliquez ici pour la télécharger](docs/media/demo.mov).

## 📸 Captures d'écran

<table>
  <tr>
    <td align="center"><b>Écran de sélection</b></td>
    <td align="center"><b>Conversation en temps réel</b></td>
  </tr>
  <tr>
    <td><img src="docs/media/screenshot-01-selection.png" alt="Écran de sélection"/></td>
    <td><img src="docs/media/screenshot-02-conversation.png" alt="Conversation"/></td>
  </tr>
  <tr>
    <td align="center"><b>Vue Olivia (EN)</b></td>
    <td align="center"><b>Logs serveur</b></td>
  </tr>
  <tr>
    <td><img src="docs/media/screenshot-03-olivia.png" alt="Vue Olivia"/></td>
    <td><img src="docs/media/screenshot-04-terminal.png" alt="Terminal serveur"/></td>
  </tr>
</table>

## 🌍 Langues supportées

    | Langue | Code | Statut |
    |--------|------|--------|
    | Français | `fr` | ✅ Supporté |
    | Anglais  | `en` | ✅ Supporté |
    | Italien  | `it` | 🔜 Prochainement |
    | Espagnol | `es` | 🔜 Prochainement |
    | Allemand | `de` | 🔜 Prochainement |

## ✨ Fonctionnalités

- 🎤 **Transcription vocale** locale via [Whisper](https://github.com/openai/whisper) (faster-whisper)
- 🌍 **Traduction bidirectionnelle** FR ↔ EN via [LibreTranslate](https://libretranslate.com/) (100% local)
- 🔄 **Temps réel** via WebSockets
- 🌐 **Interface web** — aucune installation côté client
- 🔒 **100% local** — aucune donnée envoyée sur internet
- 🖥️ **Cross-platform** — fonctionne sur Mac, Windows, Linux

## 🏗️ Architecture

```
Utilisateur A (parle) → Whisper (transcription) → LibreTranslate (traduction) → Utilisateur B (lit)
                                    ↕ WebSocket temps réel
Utilisateur B (parle) → Whisper (transcription) → LibreTranslate (traduction) → Utilisateur A (lit)
```

## 📋 Prérequis

- macOS avec [Homebrew](https://brew.sh/) (pour le setup automatique)
- Python 3.11+
- ~600 Mo d'espace disque (modèles Whisper + LibreTranslate)
- Microphone

> **Windows/Linux** : le setup manuel reste possible, voir la section ci-dessous.

## 🚀 Installation

```bash
git clone https://github.com/TON_USERNAME/projet-olivia.git
cd projet-olivia
chmod +x setup.sh start.sh
./setup.sh
```

Le script installe automatiquement FFmpeg, mkcert, les dépendances Python et télécharge les modèles.

## ▶️ Lancement

**Terminal 1 — Moteur de traduction :**
```bash
.venv/bin/libretranslate --load-only fr,en --port 5001
```

**Terminal 2 — Serveur de l'application :**
```bash
./start.sh
```

L'adresse IP locale est détectée automatiquement et affichée au démarrage.

**Utilisateur A** ouvre : `https://localhost:8000`  
**Utilisateur B** ouvre : `https://[IP-affichée]:8000`

> La première fois, le navigateur affiche un avertissement SSL (certificat auto-signé). Cliquer sur "Paramètres avancés" → "Continuer".

## 🌍 Utilisation sur internet (longue distance)

Pour une connexion entre deux pays, utilise [ngrok](https://ngrok.com/) :

```bash
brew install ngrok
ngrok config add-authtoken TON_TOKEN
ngrok http 8000
```

Partage l'URL générée (`https://xxx.ngrok-free.app`) avec l'autre utilisateur.

## 🛠️ Installation manuelle (Windows / Linux)

1. Installer [Python 3.11+](https://python.org), [FFmpeg](https://ffmpeg.org/), [mkcert](https://github.com/FiloSottile/mkcert)
2. Créer le venv : `python3 -m venv .venv`
3. Installer les dépendances : `.venv/bin/pip install -r requirements.txt`
4. Générer le certificat : `mkcert TON_IP localhost 127.0.0.1`
5. Lancer uvicorn manuellement :
```bash
.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --ssl-certfile TON_IP+2.pem --ssl-keyfile TON_IP+2-key.pem
```

## 📁 Structure du projet

```
projet-olivia/
├── main.py              # Serveur FastAPI + WebSockets + Whisper + LibreTranslate
├── start.sh             # Script de lancement (détecte l'IP automatiquement)
├── setup.sh             # Script d'installation (macOS)
├── requirements.txt     # Dépendances Python
└── static/
    ├── index.html       # Interface web
    ├── style.css        # Styles
    └── app.js           # Logique WebSocket + enregistrement audio
```

## 🗺️ Roadmap

- [x] POC — conversation FR ↔ EN sur réseau local (validé le 14/04/2026)
- [x] Synthèse vocale (TTS) — lecture automatique des traductions
- [x] Script de démarrage unique (`./start_all.sh`)
- [ ] Support d'autres langues (ES, DE, IT…)
- [ ] Test sur internet via Ngrok
- [ ] App Electron / PWA mobile

## 📄 Licence

MIT — libre d'utilisation, modification et distribution.
