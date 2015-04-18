#!/usr/bin/env python3.4

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

class ConsumerApp(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(ConsumerApp, self).__init__(parent)
        self.setupUi(self)

        self.value = 0
        self.operation = 0
        self.decimal_digits = 0
        self.checked = 0
        self.output_display.setAlignment(QtCore.Qt.AlignRight)

        self.decimaldigits.addItems('0 1 2 3 4 5'.split())
        self.decimaldigits.activated['QString'].connect(self.display_decimaldigits)
        self.separator.stateChanged.connect(self.display_separator)

        self.zero.clicked.connect(self.display_zero)
        self.one.clicked.connect(self.display_one)
        self.two.clicked.connect(self.display_two)
        self.three.clicked.connect(self.display_three)
        self.four.clicked.connect(self.display_four)
        self.five.clicked.connect(self.display_five)
        self.six.clicked.connect(self.display_six)
        self.seven.clicked.connect(self.display_seven)
        self.eight.clicked.connect(self.display_eight)
        self.nine.clicked.connect(self.display_nine)

        self.decimalpoint.clicked.connect(self.display_decimalpoint)
        self.add.clicked.connect(self.display_add)
        self.subtract.clicked.connect(self.display_subtract)
        self.multiply.clicked.connect(self.display_multiply)
        self.divide.clicked.connect(self.display_divide)
        self.equal.clicked.connect(self.display_equal)
        self.clear.clicked.connect(self.display_clear)


    def display_zero(self):
        value = self.output_display.text()
        self.output_display.setText(value + '0')

    def display_one(self):
        value = self.output_display.text()
        self.output_display.setText(value + '1')

    def display_two(self):
        value = self.output_display.text()
        self.output_display.setText(value + '2')

    def display_three(self):
        value = self.output_display.text()
        self.output_display.setText(value + '3')

    def display_four(self):
        value = self.output_display.text()
        self.output_display.setText(value + '4')

    def display_five(self):
        value = self.output_display.text()
        self.output_display.setText(value + '5')

    def display_six(self):
        value = self.output_display.text()
        self.output_display.setText(value + '6')

    def display_seven(self):
        value = self.output_display.text()
        self.output_display.setText(value + '7')

    def display_eight(self):
        value = self.output_display.text()
        self.output_display.setText(value + '8')

    def display_nine(self):
        value = self.output_display.text()
        self.output_display.setText(value + '9')

    def display_decimalpoint(self):
        value = self.output_display.text()

        if('.' not in value):
            self.output_display.setText(value + '.')

    def display_add(self):
        value = self.output_display.text().replace(',', '')

        if(value != ''):
            self.value = float(value)
            self.display_clear()
            self.operation = 1

    def display_subtract(self):
        value = self.output_display.text().replace(',', '')

        if(value != ''):
            self.value = float(value)
            self.display_clear()
            self.operation = 2

    def display_multiply(self):
        value = self.output_display.text().replace(',', '')

        if(value != ''):
            self.value = float(value)
            self.display_clear()
            self.operation = 3

    def display_divide(self):
        value = self.output_display.text().replace(',', '')

        if(value != ''):
            self.value = float(value)
            self.display_clear()
            self.operation = 4

    def display_equal(self):
        value = self.output_display.text().replace(',', '')
        self.decimal_digits = str(self.decimal_digits).replace(',', '')

        if(self.checked == 1):
            formatting = '{:,.' + str(self.decimal_digits) + 'f}'
        else:
            formatting = '{:.' + str(self.decimal_digits) + 'f}'

        if(value == ""):
            self.operation = 0
            self.value = 0
        else:
            value = float(value)
        
        if(self.operation == 0):
            self.value = value
        elif(self.operation == 1):
            self.value += value
        elif(self.operation == 2):
            self.value -= value
        elif(self.operation == 3):
            self.value *= value
        elif(self.operation == 4):
            if(value != 0):
                self.value /= value
            else:
                self.value = 0
        elif(self.operation == 5):
            self.value = value
        else:
            self.value = value

        display_val = formatting.format(self.value)
        count = 0
        the_string = ""

        for item in display_val:

            try:
                temp = int(item)

                if temp in list(range(10)):
                  count += 1
            except:
                pass

            the_string += item

            if(count == 12):
              break

        self.output_display.setText(the_string)
        self.operation = 0


    def display_clear(self):
        self.output_display.clear()
        self.output_display.setText('')

    def display_decimaldigits(self, value):
        self.decimal_digits = int(value)
        self.operation = 5
        self.display_equal()

    def display_separator(self, state):
        if(state == QtCore.Qt.Checked):
            self.checked = 1
        else:
            self.checked = 0

        self.operation = 5
        self.display_equal()


currentApp = QApplication(sys.argv)
currentForm = ConsumerApp()

currentForm.show()
currentApp.exec_()
