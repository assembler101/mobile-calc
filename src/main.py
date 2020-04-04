import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class Test(Button):
    pass

class CalcApp(App):
    def build(self):
        test = Test()

        return test

if __name__ == '__main__':
    CalcApp().run()
