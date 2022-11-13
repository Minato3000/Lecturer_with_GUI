import pyttsx3 as tts


def speak(filename):
    # Read the file `teacher_speech`
    file = open(filename, 'r')
    file_info = file.read()

    # Speak out loud using pyttsx3
    engine = tts.init()

    # Accessing `"rate"` property
    # rate = engine.getProperty("rate")
    # print(rate)
    engine.setProperty("rate", 142)

    # Accessing `"volume"` property
    engine.setProperty("volume", 0.6)

    # Accessing `"voice"` property
    voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice.name)
    engine.setProperty("voice", voices[6].id)   # Change voices[6] as it varies in systems

    engine.save_to_file(file_info, 'speech.mp3')
    engine.say(file_info)
    engine.runAndWait()

if __name__ == '__main__':
    speak("teacher_speech")
