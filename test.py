import whisper
import streamlit as st
# import soundfile as sf
# from io import BytesIO
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment

st.title("MediScribe")

state = st.session_state

st.write("Record your voice, and play the recorded audio:")
audio_file = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop Recording", key='recorder')
if audio_file is not None:
    st.audio(audio_file['bytes'])

print(audio_file)
def convert_wav_to_mp3(input_wav_bytes):
    audio = AudioSegment.from_wav(BytesIO(input_wav_bytes))
    mp3_bytes = BytesIO()
    audio.export(mp3_bytes, format="mp3")
    return mp3_bytes

output_mp3 = convert_wav_to_mp3(audio_file)


model = whisper.load_model("base")
with st.spinner("Transcription in progress..."):
    result = model.transcribe("output.mp3")
st.success("Transcribed!") #woohoo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! :3
st.write(result["text"])

# import streamlit as st
# from streamlit_mic_recorder import mic_recorder, speech_to_text

# state = st.session_state

# if 'text_received' not in state:
#     state.text_received = []

# c1, c2 = st.columns(2)
# with c1:
#     st.write("Convert speech to text:")
# with c2:
#     text = speech_to_text(language='en', use_container_width=True, just_once=True, key='STT')

# if text:
#     state.text_received.append(text)

# for text in state.text_received:
#     st.text(text)

# st.write("Record your voice, and play the recorded audio:")
# audio = mic_recorder(start_prompt="⏺️", stop_prompt="⏹️", key='recorder')

# if audio:
#     st.audio(audio['bytes'])