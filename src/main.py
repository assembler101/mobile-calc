import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty

from kivy.core.window import Window

import regex

class CalcDisplay(BoxLayout):
    resultsDsp = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.operators = {
            '+': True,
            '-': True,
            '×': True,
            '÷': True
        }

        # we will use this to clear the results when done calculations
        self.doneCalc = False

    # adds an operator or num depending on clicked button
    def addChar(self, char):
        if self.doneCalc:
            self.resultsDsp.text = ''
            self.doneCalc = False

        charStr = str(char)

        if self.operators.get(charStr):
            # add spacing for the operator
            self.resultsDsp.text += f' {charStr} '
        else:
            self.resultsDsp.text += charStr
    
    def deleteRightmostChar(self):
        # trim possible spaces due to spaces between operators
        self.resultsDsp.text = self.resultsDsp.text.rstrip()

        # delete one character of results display
        self.resultsDsp.text = self.resultsDsp.text[:-1]

        self.resultsDsp.text = self.resultsDsp.text.rstrip()

    def displayAnswer(self):
        eqn = self.resultsDsp.text

        # remove all spaces for easier computation
        eqn = eqn.replace(' ', '')

        if len(eqn) == 0 or eqn[0] == '=':
            return
        
        if len(eqn) == 0: return
        if not self.__verifyEqn(eqn):
            # display error message
            self.resultsDsp.text = 'Error'
            self.doneCalc = True

            return

        # parse the operators left to right, using BEDMAS
        answer = self.__calcValue(eqn)

        # format answer decimal places
        self.resultsDsp.text = '=' + ('%.5g' % answer)
        print('%.5f' % answer)
        self.doneCalc = True

    def __calcValue(self, eqn):
        reNumMatch = regex.compile(r'^(?:\d+\.\d*|\d*\.\d+|\d+)')
        total = 0
        prevNum = regex.match(reNumMatch, eqn).group()

        # start iteration at length of first num (prev num)
        i = len(prevNum)

        prevNum = float(prevNum)
        while i < len(eqn):
            operator = eqn[i]           
            currentNum = regex.match(reNumMatch, eqn[i+1:])
            
            if currentNum == None:
                break

            i += len(currentNum.group()) + 1
            currentNum = float(currentNum.group())

            # set current number to negative if subtract operator
            if operator == '-':
                currentNum = -currentNum
            # apply BEDMAS calculation to multiplication and division
            elif operator == '×':
                prevNum *= currentNum
                continue
            elif operator == '÷':
                prevNum /= currentNum
                continue

            total += prevNum
            prevNum = currentNum

        total += prevNum

        # don't display trailing decimal if number is int
        if total % 1 == 0:
            total = int(total)

        return total

    def __verifyEqn(self, eqn):
        numMatch = r'(?:\d+\.\d*|\d*\.\d+|\d+)'

        # use regex verification
        re = regex.compile(r'^(?:' + numMatch + '[-+×÷])*' + numMatch + '+$')

        match = regex.search(re, eqn)

        if match == None:
            return False
        return True
        
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
