from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

import lecturer_gtts as lg

Builder.load_file("lecturer_kv.kv")


class LecturerLayout(Widget):
    def selected(self, filename):
        file_text = lg.readfile(filename[0])
        lg.googlespeech(filename[0])

        self.ids.popup_label.text = "Hello I changed!!"




class LecturerApp(App):
    def build(self):
        return LecturerLayout()


if __name__ == '__main__':
    LecturerApp().run()
