import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import threading

st.set_page_config(page_title="Live Call Translator", layout="centered")
st.title("📞 Telugu ↔ English Live Call Translator")

translator = Translator()

# Speech to Text Function
def recognize_speech(language='te-IN'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak now!")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        text = recognizer.recognize_google(audio, language=language)
        st.success(f"You said: {text}")
        return text
    except Exception as e:
        st.error(f"Could not recognize speech: {e}")
        return ""

# Text to Speech Function
def speak_text(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")
        return fp.name

# Simulated Call Logic
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Telugu Speaker")
    if st.button("🎙️ Speak in Telugu"):
        telugu_text = recognize_speech(language='te-IN')
        translated = translator.translate(telugu_text, src='te', dest='en').text
        st.write(f"Translated to English: {translated}")
        speak_text(translated, lang='en')

with col2:
    st.subheader("👤 English Speaker")
    if st.button("🎙️ Speak in English"):
        english_text = recognize_speech(language='en')
        translated = translator.translate(english_text, src='en', dest='te').text
        st.write(f"Translated to Telugu: {translated}")
        speak_text(translated, lang='te')

st.markdown("---")
st.info("This is a simulated translator call. Real call and contact access is not supported on Streamlit yet.")
