#!/usr/bin/env python3.4

import re

file = "rawGrades.xml"

def openGrades(file):
  a = ""
  with open(file) as f:
    for line in f:
      a += line

  return(a)

def format(data):
  regex = r".*<students>(?P<info>.*)</students>.*"
  regex2 = r".*?<(?P<id>[A-Z0-9]{3}?)>(?P<name>.*?):(?P<person>.*?)</(?P<id2>[A-Z0-9]{3}?)>.*?"

  a = re.match(regex, data, re.S)

  b = a.group("info")

  d = re.findall(regex2, b, re.S)

  c = []

  for item in d:
    w, x, y, z = item

    if(w == z):
      c.append(item)

  master = []
  new_c = []

  for item in c:
    the_list = []
    w, x, y, z = item
    temp = y.split()
    new_c.append([w, x])

    for item in range(len(temp)):
      if(item != len(temp) - 1):
        the_string = temp[item][:-1]
        the_list.append(the_string)
      else:
        the_list.append(temp[item])

    master.append(the_list)

  scores = []

  for i in range(len(master)):
    dict = {}

    for j in range(len(master[i])):
      # HERERE
      temp = master[i][j]
      temp = temp[1:-1]
      values = temp.split(':')

      key = values[0]
      value = int(values[1])

      dict[key] = value

    scores.append(dict)

  f = open('finalGrades.xml', 'w')

  f.write('<?xml version="1.0"?>\n')
  f.write('<students>\n')

  total = []
  for item in scores:
    interim = []
    for key, value in item.items():
      interim.append([key, value])
    
    interim.sort()
    total.append(interim)

  for i in range(len(new_c)):
    f.write('   <student name="{0}" id="{1}">\n'.format(new_c[i][1], new_c[i][0]))

    for score in total[i]:
      mark = score[1]

      if(mark >= 90):
        mark = "A"
      elif(mark >= 80):
        mark = "B"
      elif(mark >= 70):
        mark = "C"
      elif(mark >= 60):
        mark = "D"
      else:
        mark = "F"

      f.write('      <ECE{0} score="{1}" grade="{2}"/>\n'.format(score[0], score[1], mark))

    f.write('   </student>\n')

  f.write('</students>')

if __name__ == "__main__":
  data = openGrades(file)
  format(data)
