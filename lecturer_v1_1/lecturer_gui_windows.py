from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import lecturer_gtts as lg


class FilesWindow(Screen):
    def selected(self, filename):
        try:
            file_info = lg.readfile(filename[0])
            print(file_info)

        except:
            pass


class ContentWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("lecturer_windows.kv")


class LecturerApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    LecturerApp().run()
