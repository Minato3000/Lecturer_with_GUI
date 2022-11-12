import kivy
from kivy.app import App
from kivy.uix.label import Label


class HelloKivy(App):
    def click_kritto(self, instance, value):
        print("You clicked Kritto!!!")
    def build(self):
        kritto = Label(text = "[color=33ff33]Hello [ref=kritto][b]Kritto[/b][/ref][/color]",
                     font_size = "50",
                     markup = True
                     )
        kritto.bind(on_ref_press = self.click_kritto)
        return kritto

kivyApp = HelloKivy()
kivyApp.run()