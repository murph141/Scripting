#!/usr/bin/env python3

import glob

def generateReportForAllUsers():

    a = glob.glob('./reports/*')

  master = {}
  names = helper()

  for item in a:
      with open(item, 'r') as f:
          content = f.read()

      content = content.split()
      id = content[2]
      name = names[id]
      content = content[8:]

      units = []
      cost = []

      for i in range(0, len(content), 4):
          cost.append(float(content[i + 3][1:]))
        units.append((int(content[i + 2])))

      a = sum(cost)
      b = sum(units)

      if name in master:
          un, sp = master[name]
        master[name] = (un + b, sp + a)
    else:
        master[name] = (b, a)

  return(master)


def helper():

    master = {}

  with open('./users.txt', 'r') as f:
      content = f.read()

    content = content.split()
    content = content[5:]

    for i in range(0, len(content), 4):
        name = content[i][:-1] + " " + content[i + 1]
      master[content[i + 3]] = name

  return(master)


def generateReportForAllViruses():

    a = glob.glob('./reports/*')

  master = {}

  for item in a:
      with open(item, 'r') as f:
          content = f.read()

      content = content.split()
      content = content[8:]

      units = []
      cost = []
      virus = []

      for i in range(0, len(content), 4):
          virus.append(content[i + 1])
        units.append(int(content[i + 2]))
        cost.append(float(content[i + 3][1:]))

      for i in range(len(virus)):
          v = virus[i]
        c = units[i]
        b = cost[i]

        if v in master:
            un, co = master[v]
          master[v] = (un + c, b + co)
      else:
          master[v] = (c, b)

  print(master)


def getUsersWithoutReports():

    names = helper()

  master = generateReportForAllUsers()

  name = []
  s = set()

  for key, value in names.items():
      name.append(str(value))


  for n in name:

      if n not in master:
          s.add(n)

  return(s)


def getTotalSpending():

    master = generateReportForAllUsers()

  sum = 0

  for key, value in master.items():
      a, b = value
    sum += b

  return(sum)
