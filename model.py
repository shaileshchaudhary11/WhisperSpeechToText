import torch
import librosa
import ffmpeg
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

# Initialize processor and model
processor = AutoProcessor.from_pretrained("openai/whisper-large-v2")
model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-large-v2")

def convert_audio(input_path, output_path):
    # Convert MP3 to WAV using ffmpeg
    ffmpeg.input(input_path).output(output_path).run()

def prepare_audio(audio_file_path):
    audio, _ = librosa.load(audio_file_path, sr=16000)  # Load audio at 16kHz sampling rate
    return audio

def transcribe_audio(audio_file_path):
    # Convert audio file to WAV
    output_audio_file_path = "audio.wav"
    convert_audio(audio_file_path, output_audio_file_path)
    
    # Load audio
    audio_input = prepare_audio(output_audio_file_path)
    
    # Transcribe
    input_features = processor(audio_input, return_tensors="pt").input_features
    generated_ids = model.generate(input_features)
    
    # Decode
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return transcription
