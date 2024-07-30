import streamlit as st
from model import transcribe_audio

# Streamlit UI
st.title("Audio Transcription")

uploaded_file = st.file_uploader("Choose an audio file (MP3)", type="mp3")

if uploaded_file is not None:
    # Save uploaded file
    audio_file_path = "uploaded_audio.mp3"
    with open(audio_file_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.write("File uploaded successfully!")

    # Transcribe
    if st.button("Transcribe Audio"):
        transcription = transcribe_audio(audio_file_path)
        st.write("Transcription:")
        st.write(transcription)
