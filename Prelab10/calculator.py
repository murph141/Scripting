# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created: Sun Mar 29 13:29:03 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 253)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 54, 561, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.seven = QtGui.QPushButton(self.layoutWidget)
        self.seven.setObjectName("seven")
        self.gridLayout.addWidget(self.seven, 0, 0, 1, 1)
        self.eight = QtGui.QPushButton(self.layoutWidget)
        self.eight.setObjectName("eight")
        self.gridLayout.addWidget(self.eight, 0, 1, 1, 1)
        self.nine = QtGui.QPushButton(self.layoutWidget)
        self.nine.setObjectName("nine")
        self.gridLayout.addWidget(self.nine, 0, 2, 1, 1)
        self.divide = QtGui.QPushButton(self.layoutWidget)
        self.divide.setObjectName("divide")
        self.gridLayout.addWidget(self.divide, 0, 3, 1, 1)
        self.clear = QtGui.QPushButton(self.layoutWidget)
        self.clear.setMinimumSize(QtCore.QSize(0, 60))
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 0, 4, 2, 1)
        self.four = QtGui.QPushButton(self.layoutWidget)
        self.four.setObjectName("four")
        self.gridLayout.addWidget(self.four, 1, 0, 1, 1)
        self.five = QtGui.QPushButton(self.layoutWidget)
        self.five.setObjectName("five")
        self.gridLayout.addWidget(self.five, 1, 1, 1, 1)
        self.six = QtGui.QPushButton(self.layoutWidget)
        self.six.setObjectName("six")
        self.gridLayout.addWidget(self.six, 1, 2, 1, 1)
        self.multiply = QtGui.QPushButton(self.layoutWidget)
        self.multiply.setObjectName("multiply")
        self.gridLayout.addWidget(self.multiply, 1, 3, 1, 1)
        self.one = QtGui.QPushButton(self.layoutWidget)
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 2, 0, 1, 1)
        self.two = QtGui.QPushButton(self.layoutWidget)
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 2, 1, 1, 1)
        self.three = QtGui.QPushButton(self.layoutWidget)
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 2, 2, 1, 1)
        self.subtract = QtGui.QPushButton(self.layoutWidget)
        self.subtract.setObjectName("subtract")
        self.gridLayout.addWidget(self.subtract, 2, 3, 1, 1)
        self.equal = QtGui.QPushButton(self.layoutWidget)
        self.equal.setMinimumSize(QtCore.QSize(0, 60))
        self.equal.setObjectName("equal")
        self.gridLayout.addWidget(self.equal, 2, 4, 2, 1)
        self.zero = QtGui.QPushButton(self.layoutWidget)
        self.zero.setObjectName("zero")
        self.gridLayout.addWidget(self.zero, 3, 0, 1, 2)
        self.decimalpoint = QtGui.QPushButton(self.layoutWidget)
        self.decimalpoint.setObjectName("decimalpoint")
        self.gridLayout.addWidget(self.decimalpoint, 3, 2, 1, 1)
        self.add = QtGui.QPushButton(self.layoutWidget)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 3, 3, 1, 1)
        self.separator = QtGui.QCheckBox(Form)
        self.separator.setGeometry(QtCore.QRect(350, 214, 223, 22))
        self.separator.setObjectName("separator")
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 214, 205, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.decimaldigits = QtGui.QComboBox(self.splitter)
        self.decimaldigits.setObjectName("decimaldigits")
        self.output_display = QtGui.QLabel(Form)
        self.output_display.setGeometry(QtCore.QRect(10, 20, 561, 21))
        self.output_display.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.output_display.setText("")
        self.output_display.setObjectName("output_display")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Eric Murphy - Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.seven.setText(QtGui.QApplication.translate("Form", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.eight.setText(QtGui.QApplication.translate("Form", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.nine.setText(QtGui.QApplication.translate("Form", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.divide.setText(QtGui.QApplication.translate("Form", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.clear.setText(QtGui.QApplication.translate("Form", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.four.setText(QtGui.QApplication.translate("Form", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.five.setText(QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.six.setText(QtGui.QApplication.translate("Form", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.multiply.setText(QtGui.QApplication.translate("Form", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.one.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.two.setText(QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.three.setText(QtGui.QApplication.translate("Form", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.subtract.setText(QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.equal.setText(QtGui.QApplication.translate("Form", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.zero.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.decimalpoint.setText(QtGui.QApplication.translate("Form", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.add.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.separator.setText(QtGui.QApplication.translate("Form", "Display Thousand\'s Separator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Decimal Digits", None, QtGui.QApplication.UnicodeUTF8))

