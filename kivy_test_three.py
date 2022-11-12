import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color: "))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        self.submit = Button(on_press=self.press)
        self.add_widget(self.submit)

    # def press(self, instance):
    #     name = self.name.text
    #     pizza = self.pizza.text
    #     color = self.color.text
    #
    #     self.add_widget(Label(text=f'Hello {name}, so you like {pizza} pizza, and your favorite color is {color}'))


class MyApp(App):
    def build(self):
        return MyGridLayout


if __name__ == '__main__':
    MyApp().run()