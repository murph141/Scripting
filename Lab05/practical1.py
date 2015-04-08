#!/usr/bin/env python3.4

def getListProduct(numList):
  if(len(numList) == 0):
    return(0)

  product = 1

  for item in numList:
    product *= item

  return(product)


def partition(numList, n):

  for i in range(len(numList) - n + 1):
    partition = []

    partition.append(numList[i:i+n])

  return(partition)


def getLargestPartition(numList, n):
  part = partition(numList, n)

  max = 0
  list = []

  for item in part:
    a = getListProduct(item)

    if(a > max):
      max = a
      list = item

  return(list, max)

def getMatrixSize(matrix):

  row = 0
  column = len(matrix[0])

  for item in matrix:
    row += 1
  
  return([row, column])


def transposeMatrix(matrix):
  [row, col] = getMatrixSize(matrix)

  joined = []
  for i in range(col):
    for item in matrix:
      joined.append(item[i])

  trans = []
  for i in range(col):
    trans.append(joined[i*row:i*row+row])

  return(trans)

def getLargestProduct():
  values = []

  with open("Number Grid.txt") as f:
    content = f.read()

    content = content.split()

    content = list(map(int, content))

    for i in range(20):
      values.append(content[20*i:20*i+20])

  max = 0
  the_list = []
  orientation = 'H'

  for item in values:
    plist, prod = getLargestPartition(item, 4)

    if(prod > max):
      max = prod
      the_list = plist

  new_values = transposeMatrix(values)

  for item in new_values:
    plist, prod = getLargestPartition(item, 4)

    if(prod > max):
      max = prod
      the_list = plist
      orientation = 'V'

  return(the_list, max, orientation)


def getDirectory():
  content = []

  with open("Phone Directory.txt") as f:
    content = f.read()

    content = content.split()

  master = {}

  for i in range(0,len(content), 5):
    master[(content[i], content[i+1], content[i+2])] = str(content[i+3]) + ' ' + str(content[i+4])

  return(master)


def getPhoneByPartialName(pName):
  numbers = []

  directory = getDirectory()

  for key, value in directory.items():
    f, _, l = key

    if(pName == f):
      numbers.append(value)
    elif(pName == l):
      numbers.append(value)

  return(numbers)

def reverseLookup(areaCode):
  people = []

  directory = getDirectory()

  for key, value in directory.items():
    value = str(value[1:4])

    f, m, l = key

    if(areaCode == value):
      people.append(f + ' ' + m + ' ' + l)

  return(people)

if __name__ == "__main__":
  pass
