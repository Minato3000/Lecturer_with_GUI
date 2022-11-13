from gtts import gTTS
from playsound import playsound

import os

file = open("teacher_speech", 'r')
file_info = file.read()

language = 'en'

audio = gTTS(text=file_info, lang=language, slow=False)

audio.save("speech.mp3")

try:
    playsound("speech.mp3")
except:
    pass

os.remove("speech.mp3")
