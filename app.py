import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Telugu ↔ English Call Translator", layout="centered")

st.title("📞 Live Call Translator – Telugu ↔ English")
st.markdown("Simulated call translator between **Telugu and English**")
st.markdown("⚠️ Real phone/mic calls not supported (text + audio only)")

def translate_and_speak(text, source, target):
    translation = GoogleTranslator(source=source, target=target).translate(text)
    st.write(f"🔄 Translated to `{target}`: {translation}")
    tts = gTTS(translation, lang=target)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        st.audio(f.name, format="audio/mp3")

st.header("👤 Telugu Speaker")
telugu_text = st.text_input("Speak (or type) in Telugu:")
if telugu_text:
    translate_and_speak(telugu_text, source='te', target='en')

st.header("👤 English Speaker")
english_text = st.text_input("Speak (or type) in English:")
if english_text:
    translate_and_speak(english_text, source='en', target='te')

st.markdown("---")
st.markdown("👨‍💻 Developed by **Gattu Navaneeth Rao**")
