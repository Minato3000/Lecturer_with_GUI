from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('the.kv')


class filescreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        theapp.screenm.current = 'second screen'

    def change_text(self):
        textfile = "hello this is a custom text"
        theapp.secscreen.ids.lb.text = textfile


class secscreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        theapp.screenm.current = 'first screen'

    def change_color(self):
        theapp.filescreen.ids.lb.color = [1, 0, 0, 1]
        theapp.filescreen.ids.lb.text = 'color has been changed'


class theapp(App):
    def build(self):
        self.screenm = ScreenManager()
        self.filescreen = filescreen()
        screen = Screen(name="first screen")
        screen.add_widget(self.filescreen)
        self.screenm.add_widget(screen)

        self.secscreen = secscreen()
        screen = Screen(name="second screen")
        screen.add_widget(self.secscreen)
        self.screenm.add_widget(screen)

        return self.screenm


if __name__ == "__main__":
    theapp = theapp()
    theapp.run()