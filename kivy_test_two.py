import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder

kivy_as_a_file = Builder.load_file("mynewkivy.kv")


# class MyNewWidget(Widget):
#     pass


class MyNewKivyApp(App):
    def build(self):
        # return Button()
        # return MyNewWidget()
        return kivy_as_a_file

if __name__ == '__main__':
    kv_app = MyNewKivyApp()
    kv_app.run()