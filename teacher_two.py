import pyttsx3 as tts

# Read the file `teacher_speech`
file = open("teacher_speech", 'r')
file_info = file.read()

# Speak out loud using pyttsx3
engine = tts.init()
engine.setProperty("rate", 178)
engine.say(file_info)
engine.runAndWait()
