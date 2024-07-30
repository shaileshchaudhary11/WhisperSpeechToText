# Whisper-Speech-to-Text

WhisperSpeechToText is a robust audio-to-text converter leveraging the powerful Whisper model. This project uses Streamlit for a user-friendly web interface, torch for deep learning capabilities, librosa for audio processing, and transformers for model integration.

## Features

- User-Friendly Interface: Built with Streamlit, providing an easy-to-use web interface.
- High-Quality Transcription: Utilizes the Whisper model for accurate speech-to-text conversion.
- Efficient Audio Processing: Powered by librosa and ffmpeg-python for seamless audio handling.
- Model Integration: Employs transformers for smooth integration with Whisper and other models.

## Installation
To get started, clone this repository and install the required dependencies:
```
git clone https://github.com/yourusername/WhisperSpeechToText.git
cd WhisperSpeechToText
```

pip install -r requirements.txt

## Usage
Run the Streamlit app to start converting audio to text:

```
streamlit run app.py
```
## File Overview
- app.py: The main Streamlit application file.
- model.py: Contains the model loading and audio transcription logic.
- requirements.txt: Lists all the dependencies required to run the application.
  
## Requirements
- Python 3.7+
- Streamlit
- Torch
- Librosa
- FFMPEG-Python
- Transformers

## Example
- Upload an audio file using the Streamlit interface.
- Click the "Transcribe" button.
- The transcribed text will be displayed on the web page.
