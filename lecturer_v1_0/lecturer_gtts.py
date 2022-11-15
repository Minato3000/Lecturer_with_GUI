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
    audio.save("audio_files/audiofile.mp3")


def textspeech(text):
    audio = gTTS(text=text, slow=False)
    audio.save("audio_files/audiofile.mp3")


def speak():
    entries = os.listdir('audio_files/')
    for entry in entries:
        playsound(entry)


