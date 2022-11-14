import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import lecturer_gtts as lg
from delete_file import *
Builder.load_file("lecturer_kv.kv")


class LecturerLayout(BoxLayout):
    def selected(self, filename):
        try:
            delete_files()
            for entry in filename:
                f = open("{}".format(entry), "r")
                text = ('''{}'''.format(f.read()))
                file = open("text_files/{}".format(os.path.split(entry)[1]), 'w')
                file.write(text)
                file.close()
            file_text = lg.readfile(filename[0])
            lg.googlespeech(filename[0])

            self.ids.filename_label.text = filename[0]

        except:
            pass


    def openfile(self):
        content = {}
        entries = os.listdir('text_files/')
        for entry in entries:
            f = open("text_files/{}".format(entry), "r")
            text = ('''{}'''.format(f.read()))
            content[entry] = text
        print(content)

    def speakfile(self):
        print("Clicked speak")
        lg.speak()



class LecturerApp(App):
    def build(self):
        return LecturerLayout()


if __name__ == "__main__":
    LecturerApp().run()
