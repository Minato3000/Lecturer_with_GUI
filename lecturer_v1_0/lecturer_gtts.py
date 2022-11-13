from gtts import gTTS
from playsound import playsound

import os


def readfile(filename):
    file = open(filename, 'r')
    file_info = file.read()
    return file_info


def googlespeech(filename):
    file_info = readfile(filename)
    print(file_info)

    audio = gTTS(text=file_info, slow=False)
    audio.save("audiofile.mp3")
