import os
import datetime
import streamlit as st
import whisper
import tempfile
from gtts import gTTS
import librosa
from audio_recorder_streamlit import audio_recorder

# Supported languages and their codes
LANGUAGES = {
    "Arabic": "ar", "Chinese (Mandarin)": "zh", "Chinese (Cantonese)": "zh-CN", "Czech": "cs",
    "Danish": "da", "Dutch": "nl", "English (US)": "en", "English (UK)": "en-GB",
    "English (Australia)": "en-AU", "Finnish": "fi", "French": "fr", "German": "de",
    "Greek": "el", "Hebrew": "he", "Hungarian": "hu", "Italian": "it", "Japanese": "ja",
    "Korean": "ko", "Norwegian": "no", "Polish": "pl", "Portuguese (Brazil)": "pt",
    "Portuguese (Portugal)": "pt-PT", "Romanian": "ro", "Russian": "ru", "Spanish": "es",
    "Swedish": "sv", "Turkish": "tr", "Ukrainian": "uk", "Vietnamese": "vi", "Urdu": "ur", "Punjabi": "pa"
}

# Set page config
st.set_page_config(page_title="STATS", layout="wide")

# Custom styles
st.markdown("""
    <style>
        .main {
            background-color: white;
        }
        .block-container {
            padding: 2rem;
        }
        h1, h2, h3 {
            color: #4DA8DA;
        }
        .stButton>button {
            background-color: #4DA8DA;
            color: White;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            border: none;
        }
        .stSelectbox, .stTextArea, .stFileUploader, .stAudio {
            background-color: #FFD66B !important;
            border-radius: 10px;
            padding: 0.3rem;
        }
        .stTabs [data-baseweb="tab-list"] {
            background-color: #80D8C3;
            border-radius: 10px 10px 0 0;
            padding: 0.5rem;
        }
        .stTabs [data-baseweb="tab"] {
            color: black;
            font-weight: bold;
        }
        .stTabs [aria-selected="true"] {
            background-color: #F5F5F5 !important;
            border-radius: 10px 10px 0 0;
        }
        .fixed-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #4DA8DA;
            color: white;
            text-align: center;
            padding: 0.5rem;
            font-size: 14px;
            z-index: 100;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

def generate_tts(text, lang_code):
    tts = gTTS(text=text, lang=lang_code)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tts.save(tmp_file.name)
        return tmp_file.name

def transcribe(audio_data, model):
    return model.transcribe(audio_data, fp16=False, verbose=False)

def save_audio_file(audio_bytes, file_extension):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"audio_{timestamp}.{file_extension}"
    with open(file_name, "wb") as f:
        f.write(audio_bytes)
    return file_name

def transcribe_audio(file_path, model):
    audio_data, sample_rate = librosa.load(file_path, sr=16000, mono=True)
    transcript = transcribe(audio_data, model)
    return transcript["text"]

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

model = load_whisper()

st.title("🗣️ STATS - Speech to Text and Text to Speech Generator")

# Tabs for functionality
tab1, tab2 = st.tabs(["🔊 Text to Speech", "🎙️ Speech to Text"])

# TEXT TO SPEECH TAB
with tab1:
    st.header("🔊 Text to Speech")
    language = st.selectbox("Select Language", list(LANGUAGES.keys()), key="tts_lang")
    lang_code = LANGUAGES[language]
    text_input = st.text_area("Enter text to synthesize", height=150, key="tts_text")

    if st.button("Generate Speech"):
        if text_input:
            tts_file_path = generate_tts(text_input, lang_code)
            st.success("Speech generated successfully!")
            st.audio(tts_file_path, format="audio/mp3")
        else:
            st.error("Please enter some text to generate speech.")

# SPEECH TO TEXT TAB
with tab2:
    st.header("🎙️ Speech to Text")

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "mp4", "wav", "m4a"])
    uploaded_filename = None
    if uploaded_file:
        ext = uploaded_file.type.split("/")[1]
        uploaded_filename = save_audio_file(uploaded_file.read(), ext)
        st.success(f"Uploaded audio saved: {uploaded_filename}")
        st.audio(uploaded_filename)

    audio_bytes = audio_recorder()
    recorded_file = None
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        recorded_file = save_audio_file(audio_bytes, "mp3")
        st.success(f"Recorded audio saved: {recorded_file}")

    if st.button("Transcribe"):
        try:
            file_to_transcribe = uploaded_filename or recorded_file
            if not file_to_transcribe:
                st.error("No audio file available. Please upload or record one.")
            else:
                transcription_result = transcribe_audio(file_to_transcribe, model)
                st.subheader("Transcription Result")
                st.write(transcription_result)
        except Exception as e:
            st.error(f"Transcription failed: {str(e)}")

# Fixed footer
st.markdown("""
<div class="fixed-footer">
    Designed and Developed by Natural Language Processing Lab, <br>
    Artificial Intelligence Technology Centre (AITeC) | National Centre for Physics (NCP)
</div>
""", unsafe_allow_html=True)
