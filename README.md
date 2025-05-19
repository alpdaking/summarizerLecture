# Lecture Summarizer

This project extracts transcripts from lecture videos and generates concise, detail-rich summaries using Google’s Gemini large language model (LLM).

---

## Features

- **Video transcription** using OpenAI Whisper  
- **Summarization** powered by Google Gemini (PaLM API)  
- Supports large transcripts with potential for RAG integration  
- Clean, modular Python code for easy integration

---

## Requirements

- Python 3.8+  
- Google Cloud account with PaLM API enabled and API key  
- FFmpeg installed (required by `moviepy` for audio extraction)  

---

## Setup

1. Clone the repo and make sure your system is ready:

   ```bash
   git clone https://github.com/yourusername/lecture-summarizer.git
   cd lecture-summarizer
   pip install -r requirements.txt
   export GEMINI_API_KEY="your_api_key_here"  # macOS/Linux
    setx GEMINI_API_KEY "your_api_key_here"   # Windows PowerShell
    ffmpeg -version

2. Start trying it out! Check out app.py.



