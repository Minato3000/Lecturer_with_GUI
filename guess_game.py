import speech_recognition as sr
import pyttsx3
import random


def listener(recognizer, microphone):
    with microphone as source:
        print("listening...")
        audio = recognizer.listen(source)
        return audio


def textConverter(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(text)
        return text
    except Exception as e:
        exception = "It is unexpected " + str(e)
        return exception

def lecturer(command):
    engine = pyttsx3.init()
    engine.setProperty("rate", 178)
    engine.say(command)
    engine.runAndWait()


if __name__ == "__main__":
    rec = sr.Recognizer()
    mic = sr.Microphone()
    words = ['apple', 'orange', 'lemon', 'pineapple', 'grapes']

    thought = random.choice(words)
    print("Words: ", end=" ")
    print(*words, sep=', ')
    print("I have thought of a word from the list of words in front of you...")
    print("Guess what the word is...")

    lecturer("I have thought of a word from the list of words in front of you...")
    lecturer("Guess what the word is...")

    chance = 3
    found = False
    while chance and not found:
        chance = chance - 1
        guess_audio = listener(rec, mic)
        guess_text = textConverter(rec, guess_audio)
        print("You: "+ guess_text)

        if guess_text == thought:
            print("Cool you found it!\n")
            lecturer("Yeah amazing, you found the word")
            found = True
        elif guess_text not in words:
            print("No only the words listed previously\n")
            lecturer("Ohh oh, I only know the words listed above...")
        elif guess_text != thought and chance>=1:
            print("No guess again\n")
            lecturer("No take another chance... guess again")

    if not found:
        print("You lost the game\n\nBetter luck next time")
        lecturer("you lost... try again later kid...")