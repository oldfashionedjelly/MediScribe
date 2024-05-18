import whisper
import streamlit as st
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
from io import BytesIO
import soundfile as sf

st.title("MediScribe")

# Function to convert WAV bytes to MP3
def convert_wav_to_mp3(input_wav_bytes):
    with BytesIO(input_wav_bytes) as wav_io:
        audio = AudioSegment.from_file(wav_io, format="wav")
        mp3_bytes = BytesIO()
        audio.export(mp3_bytes, format="mp3")
    return mp3_bytes

# Record audio
st.write("Record a conversation:")
audio_file = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop Recording", format="wav", key='recorder')

if audio_file is not None:
    st.audio(audio_file['bytes'])
    try:
        # Debug: Save the raw bytes to a file for inspection
        with open("debug.wav", "wb") as debug_file:
            debug_file.write(audio_file['bytes'])

        # Check if audio data is valid by attempting to read it with soundfile
        audio_data, samplerate = sf.read(BytesIO(audio_file['bytes']))

        # Convert recorded WAV audio to MP3
        mp3_bytes = convert_wav_to_mp3(audio_file['bytes'])

        # Save MP3 to a file
        with open('output.mp3', 'wb') as f:
            f.write(mp3_bytes.getbuffer())

        # Load Whisper model and transcribe audio
        model = whisper.load_model("base")
        with st.spinner("Transcription in progress..."):
            result = model.transcribe('output.mp3')
        
        st.success("Transcription completed!")
        st.write(result["text"])
    except Exception as e:
        st.error(f"An error occurred during audio processing: {e}")
else:
    st.write("No audio recorded yet. Please record your voice.")
