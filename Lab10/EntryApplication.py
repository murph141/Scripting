#!/usr/bin/env python3.4

import sys
import re

from PySide.QtGui import *

from EntryForm import *

class EntryApplication(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        self.states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)

        self.txtFirstName.setText('')
        self.txtLastName.setText('')
        self.txtAddress.setText('')
        self.txtCity.setText('')
        self.txtState.setText('')
        self.txtZip.setText('')
        self.txtEmail.setText('')

        self.txtFirstName.textChanged.connect(self.enableSave)
        self.txtLastName.textChanged.connect(self.enableSave)
        self.txtAddress.textChanged.connect(self.enableSave)
        self.txtCity.textChanged.connect(self.enableSave)
        self.txtState.textChanged.connect(self.enableSave)
        self.txtZip.textChanged.connect(self.enableSave)
        self.txtEmail.textChanged.connect(self.enableSave)

        self.btnClear.clicked.connect(self.clearFields)
        self.btnSave.clicked.connect(self.saveFields)
        self.btnLoad.clicked.connect(self.loadFields)

    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """

        self.filePath = filePath

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadFromXmlFile(filePath)

    def clearFields(self):
        self.txtFirstName.setText('')
        self.txtLastName.setText('')
        self.txtAddress.setText('')
        self.txtCity.setText('')
        self.txtState.setText('')
        self.txtZip.setText('')
        self.txtEmail.setText('')
        self.btnLoad.setEnabled(True)
        self.btnSave.setEnabled(False)

    def saveFields(self):
        FirstName = self.txtFirstName.text()
        LastName = self.txtLastName.text()
        Address = self.txtAddress.text()
        City = self.txtCity.text()
        State = self.txtState.text()
        Zip = self.txtZip.text()
        Email = self.txtEmail.text()

        regex = r"\w+@\w+\.\w+"

        error = 1

        if(FirstName == ''):
            self.lblError.setText('Error: First Name is not valid!')
        elif(LastName == ''):
            self.lblError.setText('Error: Last Name is not valid!')
        elif(Address == ''):
            self.lblError.setText('Error: Address is not valid!')
        elif(City == ''):
            self.lblError.setText('Error: City is not valid!')
        elif(State not in self.states):
            self.lblError.setText('Error: State is not valid!')
        elif(len(Zip) != 5 or not self.isNumber(Zip)):
            self.lblError.setText('Error: Zip is not valid!')
        elif(re.match(regex, Email) == None):
            self.lblError.setText('Error: Email is not valid!')
        else:
            self.lblError.setText('')
            error = 0

        if(not error):
            f = open("target.xml", "w")
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<user>\n')
            f.write('\t<FirstName>{}</FirstName>\n'.format(FirstName))
            f.write('\t<LastName>{}</LastName>\n'.format(LastName))
            f.write('\t<Address>{}</Address>\n'.format(Address))
            f.write('\t<City>{}</City>\n'.format(City))
            f.write('\t<State>{}</State>\n'.format(State))
            f.write('\t<ZIP>{}</ZIP>\n'.format(Zip))
            f.write('\t<Email>{}</Email>\n'.format(Email))
            f.write('<user>\n')
    
    def isNumber(self, num):
        num = str(num)

        for item in num:
            try:
                item = int(item)
            except:
                return(0)

        return(1)

    def loadFields(self):
        self.loadData()

        with open(self.filePath, 'r') as f:
            data = f.read()

        regex = r".*?<FirstName>(?P<FirstName>.*?)</FirstName>.*?<LastName>(?P<LastName>.*?)</LastName>.*?<Address>(?P<Address>.*?)</Address>.*?<City>(?P<City>.*?)</City>.*?<State>(?P<State>.*?)</State>.*?<ZIP>(?P<Zip>.*?)</ZIP>.*?<Email>(?P<Email>.*?)</Email>.*?"

        a = re.match(regex, data, re.S)

        FirstName = a.group("FirstName")
        LastName = a.group("LastName")
        Address = a.group("Address")
        City = a.group("City")
        State = a.group("State")
        Zip = a.group("Zip")
        Email = a.group("Email")

        self.txtFirstName.setText(FirstName)
        self.txtLastName.setText(LastName)
        self.txtAddress.setText(Address)
        self.txtCity.setText(City)
        self.txtState.setText(State)
        self.txtZip.setText(Zip)
        self.txtEmail.setText(Email)

    def enableSave(self):
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()
