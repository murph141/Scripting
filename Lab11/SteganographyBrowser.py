#!/usr/bin/env python3.4

# Import PySide classes
from PySide.QtCore import *
from PySide.QtGui import *

import glob, os, sys
from NewSteganography import *
from SteganographyGUI import *

# Main GUI
class ConsumerApp(QMainWindow, Ui_MainWindow):

    # Constructor
    def __init__(self, parent=None):
        super(ConsumerApp, self).__init__(parent)
        self.setupUi(self)

        # No directory has been selected yet
        self.directory = ''

        # Loop until the user returns a valid directory from the file dialog
        self.directory = self.showDialog()

        if(self.directory == ''):
            sys.exit(1)

        # Examine whether the images have messages or not
        self.examineImages()

        # Turn certain properties on or off
        self.btnExtract.setDisabled(True)
        self.btnWipeMedium.setDisabled(True)
        self.lblImageMessage.setDisabled(True)
        self.viewMedium.setHidden(True)
        self.viewMessage.setHidden(True)
        self.txtMessage.setHidden(True)

        # Connect the clicked functions
        self.btnExtract.clicked.connect(self.extracting)
        self.btnWipeMedium.clicked.connect(self.confirmWipe)
        self.fileTreeWidget.itemClicked.connect(self.treeClicked)

    # If any of the items in the tree were clicked
    def treeClicked(self):
        # Get the current item
        a = self.fileTreeWidget.currentItem()

        # Clear the two graphics views in the stackedWidget
        self.txtMessage.clear()
        tempScene = QGraphicsScene()
        self.viewMessage.setScene(tempScene)
        
        # Check the type of data that was sent back
        if(type(a.data(0, 1)) == type(None)):
            pass
        elif(len(a.data(0, 1)) == 3):
            # Enable a few things
            self.lblTextMessage.setDisabled(False)
            self.lblImageMessage.setDisabled(False)
            
            # Save the returned data
            self.imagePath, self.imageDirection, self.imageType = a.data(0, 1)
            self.data = a.data(0, 1)

            # Check for the image type, and switch indices
            if(self.imageType == 'Text'):
                self.stackMessage.setCurrentIndex(1)
            else:
                self.stackMessage.setCurrentIndex(0)

            # Enable a couple of things
            self.viewMedium.setHidden(False)
            self.btnExtract.setDisabled(False)
            self.btnWipeMedium.setDisabled(False)

            # Check for the image type, and clear accordingly
            if(self.imageType == 'Text'):
                self.lblImageMessage.clear()
                self.lblTextMessage.setText('Text')
            else:
                self.lblImageMessage.setText('Image')
                self.lblTextMessage.clear()

            # Enable a couple of things
            self.viewMessage.setHidden(False)
            self.txtMessage.setHidden(False)
        else:
            # Set the type of message
            self.lblTextMessage.clear()
            self.lblImageMessage.setText('Text')
            
            # Disable a couple of things
            self.lblImageMessage.setDisabled(True)
            self.lblTextMessage.setDisabled(True)

            # Save the returned data
            self.imagePath, _ = a.data(0, 1)
            self.imageDirection = ''
            self.imageType = ''
            self.data = (self.imagePath, self.imageDirection, self.imageType)

            # Disable and hide / unhide a couple of things
            self.viewMedium.setHidden(False)
            self.btnExtract.setDisabled(True)
            self.btnWipeMedium.setDisabled(True)
            self.viewMessage.setHidden(True)
            self.txtMessage.setHidden(True)

        # Paint the origin image
        newScene = QGraphicsScene()
        pixels = newScene.addPixmap(QPixmap(self.imagePath))

        self.viewMedium.setScene(newScene)
        self.viewMedium.fitInView(pixels, Qt.KeepAspectRatio)

        # Clear the text graphics view
        self.txtMessage.clear()


    # Extracting the hidden message
    def extracting(self):
        # Pull values from the saved data
        path, direction, messageType = self.data
        self.btnExtract.setDisabled(True)

        # Check for message type
        if(messageType == 'Text'):
            # Change the current index
            self.stackMessage.setCurrentIndex(1)
            
            # Extract the message from the medium, and decode the base64 encoding
            n = NewSteganography(imagePath = path, direction = direction)

            message = n.extractMessageFromMedium()
            temporary = message.getXmlString()
            _, _, message, _ = message.xmlParse(temporary)

            textMessage = base64.b64decode(bytes(message, "UTF-8")).decode("ascii")

            # Clear the current text, then insert the text message
            self.txtMessage.clear()
            self.txtMessage.insertPlainText(textMessage)

        elif(messageType in ['GrayImage', 'ColorImage']):
            # Change the current index
            self.stackMessage.setCurrentIndex(0)

            # Create a new scene
            newScene = QGraphicsScene()
            n = NewSteganography(imagePath = path, direction = direction)

            # Extract the message
            messageToDisplay = n.extractMessageFromMedium()

            # Save the message to a temp file
            messageToDisplay.saveToTarget('.temp123.png')
            pixels = newScene.addPixmap(QPixmap('.temp123.png'))

            # Paint the extracted imaged
            self.viewMessage.setScene(newScene)
            self.viewMessage.fitInView(pixels, Qt.KeepAspectRatio)
            os.remove('.temp123.png')

            # Clear the text graphics view
            self.txtMessage.clear()


    # Show the file dialog
    def showDialog(self):
        fname = QtGui.QFileDialog.getExistingDirectory(self, 'Open file', './')

        return(fname)


    # Confirm the wiping of the message
    def confirmWipe(self):
        msgBox = QMessageBox()
        msgBox.setText('Confirm Wipe')
        msgBox.setInformativeText('Are you sure you want to wipe the current medium?')
        msgBox.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msgBox.setDefaultButton(QMessageBox.No)
        ret = msgBox.exec_()

        # If the user selects yes
        if(ret == QMessageBox.Yes):
            n = NewSteganography(imagePath = self.imagePath, direction = self.imageDirection)

            # Call the wipe medium function, repopulate the origin fileTreeWidget
            n.wipeMedium()
            self.fileTreeWidget.clear()
            self.examineImages()

            # Clear the two graphics views in the stackedWidget
            self.txtMessage.clear()
            tempScene = QGraphicsScene()
            self.viewMessage.setScene(tempScene)

            self.btnWipeMedium.setDisabled(True)
            self.btnExtract.setDisabled(True)
            self.viewMessage.setHidden(True)
            self.txtMessage.setHidden(True)
            self.lblTextMessage.setText('Text')
            self.lblImageMessage.setText('Text')
            self.lblTextMessage.setDisabled(True)
            self.lblImageMessage.setDisabled(True)


    # Examine the images in the selected directory
    def examineImages(self):
        files = glob.glob(self.directory + '/*.png')

        # Iterate over the images, and determine the direction the message is hidden in, if any at all
        fileTypes = []
        for item in files:
            try:
                if(NewSteganography(imagePath = item, direction = 'horizontal').checkIfMessageExists()[0]):
                    fileTypes.append((item, 'horizontal', NewSteganography(imagePath = item, direction = 'horizontal').checkIfMessageExists()[1]))
                elif(NewSteganography(imagePath = item, direction = 'vertical').checkIfMessageExists()[0]):
                    fileTypes.append((item, 'vertical', NewSteganography(imagePath = item, direction = 'vertical').checkIfMessageExists()[1]))
                else:
                    fileTypes.append((item, None, None))
            except TypeError:
                fileTypes.append((item, None, 'a'))

        # Iterate over the information saved above
        tempList = []
        for a, b, c in fileTypes:
            temp = a.split('/')
            itemToAdd = QTreeWidgetItem([temp[-1]])

            # Add a child to the QTreeWidgetItem if there is a hidden message
            if(b in ['horizontal', 'vertical']):
                itemToAdd.setForeground(0, QtGui.QBrush(QtGui.QColor("#FF0000")))

                newItem = QTreeWidgetItem([c])
                newItem.setForeground(0, QtGui.QBrush(QtGui.QColor("#00FF00")))

                itemToAdd.setData(0, 1, (a, b, c))
                itemToAdd.addChild(newItem)
            elif (c == 'a'):
                itemToAdd.setForeground(0, QtGui.QBrush(QtGui.QColor("#000000")))
                itemToAdd.setData(0, 1, (a, a))
            else:
                itemToAdd.setForeground(0, QtGui.QBrush(QtGui.QColor("#0000FF")))
                itemToAdd.setData(0, 1, (a, a))

            tempList.append(itemToAdd)

        # Add all the QTreeWidgetItems
        self.fileTreeWidget.addTopLevelItems(tempList)
        self.fileTreeWidget


currentApp = QApplication(sys.argv)
currentForm = ConsumerApp()

currentForm.show()
currentApp.exec_()
