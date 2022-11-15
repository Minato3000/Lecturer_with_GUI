import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder

import lecturer_gtts as lg
from delete_file import *
Builder.load_file("lecturer_kv.kv")


class LecturerLayout(Screen):
    def selected(self, filename):
        try:
            delete_files()
            self.writefile(filename[0])

            self.ids.filename_label.text = filename[0]
            lg.googlespeech(filename[0])
            print(filename)

        except:
            pass


    def writefile(self, filename):
        f = open("{}".format(filename), "r")
        text = ('''{}'''.format(f.read()))
        file = open("text_files/{}".format(os.path.split(filename)[1]), 'w')
        file.write(text)
        file.close()






class NextScreen(Screen):

    def __init__(self, **kwargs):
        super(NextScreen, self).__init__(**kwargs)
        entries = os.listdir('text_files/')
        for entry in entries:
            f = open("text_files/{}".format(entry), "r")
            text = ('''{}'''.format(f.read()))
            self.ids.content.text = text

    def speakfile(self):
        lg.speak()
        print("Clicked speak")

class LecturerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LecturerLayout(name='main'))
        sm.add_widget(NextScreen(name='next'))

        return sm

if __name__ == "__main__":
    LecturerApp().run()
