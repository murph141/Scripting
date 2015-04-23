#!/usr/bin/env python3.4
#

# Author :  $Author: ee364a14 $
# Date:     $Date: 2015-04-18 14:07:46 -0400 (Sat, 18 Apr 2015) $
# HeadURL:  $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364a14/Lab11/Steganography.py $
# Revision: $Revision: 79173 $

# Imports
import sys

sys.path.append("./BitVector")

from BitVector import *
from PIL import Image
import re
import base64
import os
import string

# Message class
class Message:
    # Constructor
    def __init__(self, **kwargs):
        # Parsing regex
        self.xmlRegex = r'.*?message type="(?P<messageType>.*?)".*?size="(?P<messageSize>.*?)".*?encrypted="(?P<encryption>.*?)".*?>(?P<fileData>.*?)</message>.*?'

        # Set direction string equal to nothing
        self.direction = ''

        # If there is only one argument
        if(len(kwargs) == 1):
            # Check to make sure that the only argument is XmlString
            if('XmlString' not in kwargs.keys()):
                raise ValueError("XmlString must be present")

            fileContent = kwargs["XmlString"]
            self.filePath = ''
            self.messageType = ''

            # Parse the XmlString
            encr, type, base, size = self.xmlParse(fileContent)

            self.encryption = encr
            self.messageType = type
            self.XmlBase64 = base
            self.messageSize = size

        # If there are two arguments
        elif(len(kwargs) == 2):
            # Make sure the two arguments are the messageType and the filePath
            if('messageType' not in kwargs.keys()):
                raise ValueError("messageType must be present")

            if('filePath' not in kwargs.keys()):
                raise ValueError("filePath must be present")

            # Make sure the messageType is Text, GrayImage, or ColorImage
            if(kwargs["messageType"] not in ['Text', 'GrayImage', 'ColorImage']):
                raise ValueError("Incorrect messageType specified")

            # Make sure the filePath is not empty
            if(kwargs["filePath"] == ''):
                raise ValueError("filepath must not be empty")

            self.messageType = kwargs["messageType"]
            self.filePath = kwargs["filePath"]

            # If the file doesn't exist, raise an OSError
            if(not os.path.isfile(self.filePath)):
                raise OSError("file does not exist")

            # If you have a Text message
            if(self.messageType == 'Text'):
                # I/O Operations
                try:
                    with open(self.filePath, 'r') as f:
                        message = f.read()
                except IOError:
                    raise IOError("file cannot be read")

                # Encode the text
                self.XmlBase64 = base64.b64encode(bytes(message, "UTF-8")).decode("ascii")
                self.messageSize = len(message)

            # If you have a GrayImage message
            elif(self.messageType == 'GrayImage'):
                # I/O Operations
                try:
                    with Image.open(self.filePath) as f:
                        message = list(f.getdata())
                        self.messageSize = f.size
                except IOError:
                    raise IOError("file cannot be read")

                # Encode the pixel data
                self.XmlBase64 = base64.b64encode(bytes(message)).decode("ascii")

            elif(self.messageType == 'ColorImage'):
                # I/O Operations
                try:
                    with Image.open(self.filePath) as f:
                        red = list(f.getdata(0))
                        green = list(f.getdata(1))
                        blue = list(f.getdata(2))

                        total = red + green + blue

                        self.messageSize = f.size
                except IOError:
                    raise IOError("file cannot be read")

                # Encode the RGB pixel data
                self.XmlBase64 = base64.b64encode(bytes(total)).decode("ascii")

            # Set encryption to false (Not doing the extra credit)
            self.encryption = "False"

        # If the number of arguments is less than 1 or greater than 2, throw a ValueError
        else:
            raise ValueError("Incorrect amount of parameters provided")


    # Get the size of the message
    def getMessageSize(self):
        XmlStringLength = len(self.getXmlString())

        # Test for an empty string
        if(XmlStringLength == 0):
            raise Exception("XmlStringLength must be greater than 0")

        return(XmlStringLength)


    # Save the messsage to an Image
    def saveToImage(self, targetImagePath):
        _ = self.getXmlString()

        # Error checking
        if(targetImagePath == ''):
            raise Exception("targetTextImagePath must be non-empty")

        if(self.messageType not in ['ColorImage', 'GrayImage']):
            raise TypeError("messageType must be GrayImage or ColorImage")

        # Parse the XML
        encr, type, base, size = self.xmlParse(self.XmlString)

        # Decode the data
        data = list(base64.b64decode(bytes(base, "UTF-8")))

        # Change the type according to the type of image
        if(type == 'GrayImage'):
            type = 'L'
        else:
            type = 'RGB'

        # Parse data for a Gray Scale Image
        if(type == 'L'):
            ima = Image.new(type, size)
            ima.putdata(data)
        # Parse data for a Color Image
        else:
            ima = Image.new(type, size)
            length = int(len(data) / 3.0)
            ima.putdata([(data[i], data[i + length], data[i + 2 * length]) for i in range(length)])

        # Save the image
        ima.save(targetImagePath)


    # Save the message to a text file
    def saveToTextFile(self, targetTextFilePath):
        _ = self.getXmlString()

        # Error checking
        if(targetTextFilePath == ''):
            raise Exception("targetTextFilePath must not be empty")

        if(self.messageType != 'Text'):
            raise TypeError("messageType must be Text")

        # Parse the XML
        _, _, base, _ = self.xmlParse(self.XmlString)

        # Decode the string
        textMessage = base64.b64decode(bytes(base, "UTF-8")).decode("ascii")

        # Write the data
        f = open(targetTextFilePath, 'w')
        f.write(textMessage)


    # Save to a specific target
    def saveToTarget(self, targetPath):
        # Choose the appropriate target
        if(self.messageType == 'Text'):
            self.saveToTextFile(targetPath)
        elif(self.messageType == 'ColorImage' or self.messageType == 'GrayImage'):
            self.saveToImage(targetPath)

    # Get the XmlString from the data
    def getXmlString(self):
        # If the messageType is text, parse this way
        if(self.messageType == 'Text'):
            XmlString = '<?xml version="1.0" encoding="UTF-8"?>\n<message type="{0}" size="{1}" encrypted="{2}">\n{3}\n</message>'.format(self.messageType, self.messageSize, self.encryption, self.XmlBase64)
        # Otherwise, parse this way
        else:
            a, b = self.messageSize
            XmlString = '<?xml version="1.0" encoding="UTF-8"?>\n<message type="{0}" size="{1},{2}" encrypted="{3}">\n{4}\n</message>'.format(self.messageType, a, b, self.encryption, self.XmlBase64)

        # If any of the members are empty, raise an Exception
        if(self.messageType == '' or self.messageSize == '' or self.encryption == '' or self.XmlBase64 == ''):
            raise Exception("Member variables should not be empty")

        # Save the XmlString
        self.XmlString = XmlString

        return(XmlString)


    # Get the data from an image
    def imageData(self, image):
        openImage = Image.open(image)

        return(openImage.format, openImage.size, openImage.mode, list(openImage.getdata()))


    # Parse the XML
    def xmlParse(self, xmlString):
        # Parse using the defined regex
        values = re.search(self.xmlRegex, xmlString, re.S)

        encryption = values.group("encryption")
        messageType = values.group("messageType")
        XmlBase64 = values.group("fileData").strip()

        # Format accordingly
        if(messageType == 'Text'):
            messageSize = int(values.group("messageSize"))
        else:
            messageSizeTemp = values.group("messageSize").split(',')
            messageSize = (int(messageSizeTemp[0].strip()), int(messageSizeTemp[1].strip()))

        return(encryption, messageType, XmlBase64, messageSize)


# The Steganography class
class Steganography:
    # Constructor
    def __init__(self, imagePath, direction='horizontal'):
        # Raise an error if the direction is not horizontal or vertical
        if(direction not in ['horizontal', 'vertical']):
            raise ValueError('direction must be horizontal or vertical')

        # Open the image
        self.image = Image.open(imagePath)

        # Get the data from the image
        self.direction = direction
        self.x, self.y = self.image.size
        self.type = self.image.mode
        self.maxSize = int(self.x * self.y / 8)

        # Raise a TypeError if the image isn't gray scale
        if(self.image.mode != 'L'):
            raise TypeError("Image must be gray scale")
        
        # Get all the pixel data
        self.imageData = list(self.image.getdata())


    # Embed a message in the image
    def embedMessageInMedium(self, message, targetImagePath):
        # Get the size of the message
        if(message.messageType == 'Text'):
            messageSize = message.messageSize
        elif(message.messageType in ['ColorImage', 'GrayImage']):
            messageSize = message.messageSize[0] * message.messageSize[1]
        else:
            messageSize = 0

        # Check for a message that is too long to embed
        if(self.maxSize < messageSize):
            raise ValueError("Message size is too large")

        # Convert the XmlString to a BitVector object
        messageString = BitVector(textstring = message.getXmlString())

        # Create an empty list
        new_data = []

        # Scan horizontally
        if(self.direction == 'horizontal'):
            # Iterate over the messageString
            for i in range(len(messageString)):
                # Pull the current pixel value
                temp = self.imageData[i]

                # Mask accordingly
                if(messageString[i]):
                    temp |= 1
                else:
                    temp &= 254

                # Append the new pixel value
                new_data.append(temp)

            # Iterate over the rest of the data
            for i in range(len(messageString), len(self.imageData)):
                new_data.append(self.imageData[i])
        
        # Scan vertically
        elif(self.direction == 'vertical'):
            total = len(messageString)
            index = 0
            the_value = 0

            im = self.image

            # Create an empty list
            for i in range(len(self.imageData)):
                new_data.append('')

            # Iterate over the messageString (y to x for vertical)
            for i in range(self.x):
                for j in range(self.y):
                    temp = im.getpixel((i, j))

                    if(index != total):
                        index += 1

                        if(messageString[the_value]):
                            temp |= 1
                        else:
                            temp &= 254

                    new_data[j * self.x + i] = temp
                    the_value += 1


        # Save the image
        ima = Image.new(self.type, (self.x, self.y))
        ima.putdata(new_data)
        ima.save(targetImagePath)


    # Extract the message fom the image
    def extractMessageFromMedium(self):
        testing = ''
        im = self.image

        # Check the direction of the scanning
        if(self.direction == 'horizontal'):
            for i in range(len(self.imageData)):
                testing += str(self.imageData[i] & 1)
        elif(self.direction == 'vertical'):
            for i in range(self.x):
                for j in range(self.y):
                    testing += str(im.getpixel((i, j)) & 1)
        else:
            return(None)

        # Create a bitvector with the given bitstring (Making sure to make it a multiple of 8)
        a = BitVector(bitstring = testing)
        addition = (8 - len(a) % 8) % 8
        a += BitVector(size = addition)

        # Convert the BitVector to a string
        b = a.get_text_from_bitvector()

        # Check for a valid message
        temp = b.split('</message>')
        
        if(len(temp) != 2):
            return(None)

        # Fix the message if it is valid
        xmlMessage = temp[0] + '</message>'

        # Create a message object with the XmlString
        messageToReturn = Message(XmlString = xmlMessage)

        return(messageToReturn)
