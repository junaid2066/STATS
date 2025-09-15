# 🗣️ STATS: A Framework for Multilingual Text to Speech and Speech to Text Generation

## 📖 Description:
STATS is a Streamlit-based application that provides two-way speech processing:
- **Text-to-Speech (TTS):** Convert typed text into natural-sounding audio in multiple languages.
- **Speech-to-Text (STT):** Transcribe uploaded or recorded audio files into text using OpenAI’s Whisper model.

Built with **Streamlit, gTTS, and Whisper**, this project offers a clean, user-friendly interface with modern UI styling.

## ✨ Features:
- **🎙️ Speech-to-Text (STT):** Upload audio files (.mp3, .wav, .m4a, .mp4) or record directly.
- **🔊 Text-to-Speech (TTS):** Generate speech from text in over 30+ supported languages.+
- 📂 Audio playback after generation or upload.
- 🖥️ Web-based interface powered by Streamlit.

## ✨ Models Used:
- **🎙️ Speech-to-Text (STT):** [Open AI Whisper 1500M](https://github.com/openai/whisper)
- **🔊 Text-to-Speech (TTS):** [gTTS Google TTS](https://pypi.org/project/gTTS/), [Tactron2](https://pytorch.org/hub/nvidia_deeplearningexamples_tacotron2/) , [FastSpeech](https://github.com/ming024/FastSpeech2)
- **For Audio File Handling:** [LIBROSA](https://github.com/librosa/librosa)

## ✨ Installation:
### A. Requirements:
- Python 3.9+
- FFmpeg (required by whisper & librosa)

### B. Usage

**Text to Speech**
- Open "Text to Speech" tab.
- Select a language.
- Enter text.
- Click Generate Speech → Play or download generated audio.

**Speech to Text**
- Open "Speech to Text" tab.
- Upload an audio file OR record using the built-in recorder.
- Click Transcribe → View transcription results instantly.

## 📊 Project Status
🚀 Active Development – new features and improvements coming soon.
