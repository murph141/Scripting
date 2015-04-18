#!/usr/bin/env python3.4
#

# Author :  $Author: ee364a14 $
# Date:     $Date: 2015-02-21 16:32:29 -0500 (Sat, 21 Feb 2015) $
# HeadURL:  $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364a14/Prelab06/Part1.py $
# Revision: $Revision: 76400 $

import re

regex1 = re.compile(' a{2,5} ')
regex2 = re.compile('(\d)+.(\d)+')
regex4 = re.compile('(\d)+')
regex5 = re.compile('ECE364')
regex6 = re.compile('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')

if __name__ == "__main__":
  # Part 1.1
  #if(re.search(regex1, ' aaa ')):
  #  print("Found")

  # Part 1.2
  #print(re.sub(regex2, 'float', 'hey 12.34 yo 1.11'))

  # Part 1.3
  #print(re.subn(regex2, 'float', 'hey 12.34 yo 1.11')[1])

  # Part 1.4
  #string = r'1 + 3 , a 7a d'
  #a = re.findall(regex4, string)
  #sum = 0
  #for item in a:
  #  sum += int(item)
  #print(sum)

  # Part 1.5
  #print(re.sub(regex5, 'ECE461', 'ECE364 ECE364', count = 1))

  # Part 1.6
  #ip1 = "001.002.003.004"
  #ip2 = "127.0.0.1"
  #ip3 = "255.255.255.255"
  #ip4 = r"255.255.255.256"
  #ip5 = "25.55.29.11"

  #ips = []
  #ips.append(ip1)
  #ips.append(ip2)
  #ips.append(ip3)
  #ips.append(ip4)
  #ips.append(ip5)

  #for item in ips:
  #  a = re.findall(regex6, item)
  #  a = a[0]
  #  b, c, d, e = a
  #  a = [b, c, d, e]

  #  temp = item.split('.')

  #  if(a == temp):
  #    print(item)

  # Part 1.7
  # Searches for "e" in a string input with re.I (case insensitive searching)
  # Searches for the phrase "is a" in a string
  # Nothing, a group name hasn't been specified for the ?P's
  # Search for a string start with "I" followed like the word "like" 10+ times, followed by "you" one or two times
