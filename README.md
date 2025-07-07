
# Gemini AI Terminal Chatbot

A modern, professional, and animated terminal-based chatbot powered by Google Gemini (via LangChain) and the Rich library for a beautiful user experience.

## Features
- ✨ Professional, animated terminal UI (Rich)
- 🤖 Uses Google Gemini API (via LangChain)
- 📝 Real answers from Gemini, not fake/generated
- � Modern, user-friendly, and responsive design
- ⏳ Animated typing and loading effects
- 🔒 API key managed securely with dotenv

## Requirements
- Python 3.8+
- Gemini API key (get from Google AI Studio)

## Setup
1. Clone this repo and enter the folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your Gemini API key.

## Usage
```bash
python gemini_chatbot.py
```

## Project Structure
- `gemini_chatbot.py` — Main Gemini chatbot app (Rich UI, LangChain, Gemini)
- `requirements.txt` — Python dependencies
- `.env.example` — Example for environment variables

## How it Works
- User enters a message in the terminal.
- The app sends the message to Gemini via LangChain.
- Gemini's real answer is shown with animated typing.

## License
MIT
