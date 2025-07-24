import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Telugu ↔ English Call Translator", layout="centered")

st.title("📞 Live Call Translator – Telugu ↔ English")
st.markdown("This is a **simulated bilingual translator** for Telugu and English voice calls.")
st.markdown("ℹ️ Real phone calls are not supported, but speech translation is!")

translator = Translator()

def translate_and_speak(text, src_lang, dest_lang):
    # Translate
    translation = translator.translate(text, src=src_lang, dest=dest_lang).text
    st.write(f"🔄 Translated to `{dest_lang}`: {translation}")

    # Speak
    tts = gTTS(text=translation, lang=dest_lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")
        return translation

st.header("👤 Telugu Speaker")
telugu_text = st.text_input("Speak (or type) in Telugu:")
if telugu_text:
    translate_and_speak(telugu_text, src_lang="te", dest_lang="en")

st.header("👤 English Speaker")
english_text = st.text_input("Speak (or type) in English:")
if english_text:
    translate_and_speak(english_text, src_lang="en", dest_lang="te")

st.markdown("---")
st.markdown("👨‍💻 Developed by **Gattu Navaneeth Rao**")
