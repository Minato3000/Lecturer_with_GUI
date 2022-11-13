from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

import lecturer_pttsx3 as lr

Builder.load_file("menu.kv")


class MyLayout(Widget):
    def selected(self, filename):
        try:
            file = open(filename[0], 'r')
            file_info = file.read()
            # file_input.text = self.selection and self.selection[0] or ''

            txt = file_info
            print(txt)
            lr.speak(filename[0])
        except:
            pass


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()