import streamlit as st
from streamlit_mic_recorder import mic_recorder, speech_to_text
import io
import os
# from whisper_stt import whisper_stt

state = st.session_state
# openai.api_key = 'sk-proj-eHstyl2tLbaZWB3LWIHaT3BlbkFJl17l1Py5OiLbNxloVQlo'

if 'text_received' not in state:
    state.text_received = []

st.title("MediScribe")

c1, c2 = st.columns(2)
with c1:
    st.write("Convert speech to text:")
with c2:
    text = speech_to_text(language='en', use_container_width=True, just_once=True, key='STT')

if text:
    state.text_received.append(text)

for text in state.text_received:
    st.text(text)

st.write("Record your voice, and play the recorded audio:")
audio = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop Recording", key='recorder')

if audio:
    state.audio_data = audio['bytes']
    st.audio(audio['bytes'])

#from pydub import AudioSegment
#AudioSegment.from_file("/input/file").export("/output/file", format="mp3")

# text = whisper_stt(openai_api_key="sk-proj-eHstyl2tLbaZWB3LWIHaT3BlbkFJl17l1Py5OiLbNxloVQlo", language = 'en')  
# if text:
#     st.write(text)