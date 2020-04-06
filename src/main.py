import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty

from kivy.core.window import Window

class CalcDisplay(BoxLayout):
    resultsDsp = ObjectProperty(None)
    
    def addNum(self, num):
        # append the num to results display
        self.resultsDsp.text += str(num)

    def addOperator(self, operator):
        # append the operator to results display
        self.resultsDsp.text += f' {operator} '

    def addDecimal(self, decimal):
        self.resultsDsp.text += str(decimal)

    def deleteRightmostChar(self):
        # trim possible spaces due to spaces between operators
        self.resultsDsp.text = self.resultsDsp.text.rstrip()

        # delete one character of results display
        self.resultsDsp.text = self.resultsDsp.text[:-1]

        self.resultsDsp.text = self.resultsDsp.text.rstrip()

    def calcValue(self):
        # parse the operators left to right
        pass

class ResultsDisplay(TextInput):
    pass

class ButtonsDisplay(ButtonBehavior, GridLayout):
    pass

class CalcApp(App):
    def build(self):
        # set the window size
        Window.size = (400, 450)

        calcDisplay = CalcDisplay()

        return calcDisplay 

if __name__ == '__main__':
    CalcApp().run()
