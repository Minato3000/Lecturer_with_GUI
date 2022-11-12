import speech_recognition as sr # Speech recognition module
import pyttsx3 # Text to speech module
import webbrowser as web

r = sr.Recognizer()

path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"


def repeat(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def speakNow():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, 0.2)

        print("speak now..")
        audio = r.listen(source)
        return audio


def convertText(audio):
    myText = r.recognize_google(audio)
    myText = myText.lower()
    repeat(myText)
    return myText

    # print(myText)
    # speechText(myText)


def main():
    audio = speakNow()
    text = convertText(audio)

    try:
        dest = r.recognize_google(audio)
        print("You said: "+ dest)

        web.get(path).open(dest)

    except Exception as e:
        print("Error: "+ str(e))


if __name__ == "__main__":
    main()