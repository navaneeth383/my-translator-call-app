import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(page_title="📞 Telugu ↔ English Call Translator", layout="centered")

st.title("📞 Telugu ↔ English Call Translator")
st.markdown("Simulate a bilingual voice call between **Telugu and English** speakers.")
st.markdown("Note: This is a simulation. No real phone calls or microphones are used.")

# Simulated contact entry
contact_name = st.text_input("Enter contact name or number to call:")

call_started = st.button("📞 Make a Call")

if call_started and contact_name:
    st.success(f"Calling {contact_name}... (Simulated)")

    st.header("👤 Telugu Speaker (Caller)")
    telugu_text = st.text_input("Type in Telugu (simulate speaking):")
    if telugu_text:
        translation = GoogleTranslator(source='te', target='en').translate(telugu_text)
        st.write(f"Translated to English: {translation}")
        tts = gTTS(translation, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            tts.save(f.name)
            st.audio(f.name, format="audio/mp3")

    st.header("👤 English Speaker (Receiver)")
    english_text = st.text_input("Type in English (simulate speaking):")
    if english_text:
        translation = GoogleTranslator(source='en', target='te').translate(english_text)
        st.write(f"Translated to Telugu: {translation}")
        tts = gTTS(translation, lang='te')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            tts.save(f.name)
            st.audio(f.name, format="audio/mp3")

    if st.button("🔚 End Call"):
        st.warning(f"Call with {contact_name} ended.")

elif call_started:
    st.error("Please enter a contact name or number to start the call.")

st.markdown("---")
st.markdown("👨‍💻 Developed by **Gattu Navaneeth Rao**")
