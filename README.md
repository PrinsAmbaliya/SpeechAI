# SpeechAI - Voice Assistant

**A Python-based voice assistant using Groq AI, speech recognition, and text-to-speech.**

---

## Features
- **Listen** to voice commands (`speech_recognition`)
- **AI Responses** powered by Groq (`openai/gpt-oss-20b`)
- **Speak** replies (`pyttsx3`)
- Open **YouTube, Google, Wikipedia**
- Tell **current time**
- Play **local music**
- Save AI output in `Groqai/` folder
- Stop with **"Python Stop"**

---

## Installation

```bash
git clone https://github.com/PrinsAmbaliya/SpeechAI.git
cd SpeechAI
pip install -r requirements.txt
```

---

## Setup API Key

1.Get free key: https://console.groq.com
2.Create config.py:
```python
apikey = "your_groq_api_key_here"
```

---

## Run

```bash
python main.py
```
Say:

- "Open YouTube"
- "What is the time"
- "Using AI tell me a joke" → saved in Groqai/joke.txt
- "Python Stop" to exit

---

## Files

main.py         - Main logic
groqai.py       - Test AI call
Groqai/         - Saved AI responses
requirements.txt
