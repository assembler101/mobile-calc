import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivy.core.window import Window

class CalcDisplay(BoxLayout):
    pass

class ResultsDisplay(TextInput):
    pass

class ButtonsDisplay(GridLayout):
    pass

class CalcApp(App):
    def build(self):
        # set the window size
        Window.size = (450, 450)

        calcDisplay = CalcDisplay()

        return calcDisplay 

if __name__ == '__main__':
    CalcApp().run()
