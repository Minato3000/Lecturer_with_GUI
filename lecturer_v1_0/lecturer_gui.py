from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import lecturer_gtts as lg

Builder.load_file("lecturer_kv.kv")


class LecturerLayout(BoxLayout):
    def selected(self, filename):
        try:
            file_text = lg.readfile(filename[0])
            lg.googlespeech(filename[0])

            self.ids.filename_label.text = file_text

        except:
            pass


class LecturerApp(App):
    def build(self):
        return LecturerLayout()


if __name__ == "__main__":
    LecturerApp().run()
