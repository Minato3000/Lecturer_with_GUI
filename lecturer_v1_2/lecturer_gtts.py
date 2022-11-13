from gtts import gTTS
from playsound import playsound


def readfile(filename):
    file = open(filename, 'r')
    file_info = file.read()
    return file_info


def googlespeech(filename):
    file_info = readfile(filename)
    print(file_info)

    audio = gTTS(text=file_info, slow=False)
    audio.save("audiofile.mp3")


def speak():
    playsound("audiofile.mp3")
