#!/usr/bin/env python3.4

# Author     $Author: ee364a14 $
# Date       $Date: 2015-04-20 14:00:01 -0400 (Mon, 20 Apr 2015) $
# HeadURL    $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364a14/Lab11/NewSteganography.py $
# Revision   $Revision: 79251 $

from Steganography import *

# New Steganography class that inherits from the Steganography class
class NewSteganography(Steganography):

    # Constructor
    def __init__(self, imagePath, direction = 'horizontal'):
        self.xmlRegex = r'.*?message type="(?P<messageType>.*?)".*?'
        self.path = imagePath

        # Call Steganography's constructor
        Steganography.__init__(self, imagePath, direction)

    # Wipe the hidden message
    def wipeMedium(self):
        # Iterate through the entire image and set all the LSBs to 0
        for i in range(len(self.imageData)):
            self.imageData[i] &= 254

        # Save the image
        ima = Image.new(self.type, (self.x, self.y))
        ima.putdata(self.imageData)
        ima.save(self.path)

    # Check if a message exists in the medium
    def checkIfMessageExists(self):
        # If the message direction is horizontal
        if(self.direction == 'horizontal'):
            testing = ''

            # Iterate over 528 bits (66 ascii characters to the type, each ascii character is 8 bits)
            for i in range(528):
                try:
                    temp = self.imageData[i]
                except IndexError:
                    return(False, None)

                temp &= 1
                testing += str(temp)

            # Convert the bitstring to a bitvector, then convert that to an ascii representation
            xml = BitVector(bitstring = testing).get_text_from_bitvector()

        # If the message direction is vertical
        elif(self.direction == 'vertical'):
            testing = ''
            total = 528
            im = self.image

            # Iterate over the x and y values
            for i in range(self.x):
                for j in range(self.y):
                    # If 528 bits have been iterated over
                    if(total == 0):
                        break

                    temp = im.getpixel((i, j))
                    temp &= 1
                    testing += str(temp)
                    total -= 1

            # Convert the bitstring to a bitvector, then convert that to an ascii representation
            xml = BitVector(bitstring = testing).get_text_from_bitvector()

        else:
            # If image direction is not horizontal or vertical, then no message exists
            xml = ''

        # Search for the message type
        values = re.search(self.xmlRegex, xml, re.S)

        if(type(values) == type(None)):
            return(False, None)

        # Message type was found, set messageType to the type of message that is hidden
        messageType = values.group('messageType')

        return(True, messageType)
