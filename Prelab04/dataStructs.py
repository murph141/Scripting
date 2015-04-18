import glob as g
import re
import string

def getFiles():
  a = g.glob('./files/*.txt')

  found = []

  for file in a:
    b = re.search('./files/(.*)', file)

    if b:
      found.append(b.group(1))

  return(found)


def createStructure():

  files = getFiles()
  
  file_list = []

  for file in files:

    with open('./files/' + file, 'r') as f:
      content = f.read()
      
      fixed = []
      words = content.split()
      file =  re.search('(.*).txt', file)
      fixed.append(file.group(1))

      for item in words:
        out = "".join(i for i in item if i not in string.punctuation)
        fixed.append(out)

    file_list.append(fixed)

  return(file_list)


def getWordFrequency(file_list):

  the_dict = {}
  giant_list = []

  for file in file_list:
    
    file_name = file[0]
    file = file[1:]

    for item in file:
      giant_list.append(item)

  for item in giant_list:

    if item in the_dict:
      the_dict[item] += 1
    else:
      the_dict[item] = 1
      
  return(the_dict)


def getDuplicates(file_list):

  files = []
  words = []
  groups = []

  for file in file_list:
    files.append(file[0])
    words.append(file[1:])

  length = len(files)

  while(len(words) != 0):

    i = 0
    j = 0

    group = []
    group.append(files[i])

    while(len(words) != 1):
      j += 1

      if(len(words) == j):
        break

      if(words[i] == words[j]):
          print(files[j])
          group.append(files[j])
          del words[j]
          del files[j]
          j -= 1


    del words[i]
    del files[i]
    groups.append(group)

  master = countWords(groups, file_list)

  return(master)


def countWords(groups, files):

  length = len(groups)

  group_key = []
  master = {}

  for i in range(length):
    group_key.append(groups[i][0])

  i = 0

  for key in group_key:
    for item in files:
      if(item[0] == key):
        count = uniqueItems(item[1:])
        master[key] = (count, groups[i])
        i += 1

  return(master)


def uniqueItems(items):


  lower = []
  A = {}
  count = 0

  #for item in items:
  #  lower.append(item.lower())
  
  for item in items:
    A[item] = 1

  return(len(A))


def getPurchases():
  a = g.glob('./purchases/*')

  found = []

  for file in a:
    b = re.search('./purchases/purchase_(.*).txt', file)

    if b:
      found.append(b.group(1))

  return(found)


def getNumbers(found):
  numbers = []

  for item in found:
    with open("./purchases/purchase_" + item + ".txt") as f:
      content = f.read()

      content = content.split()
      content = content[3:]

      length = len(content)
      quantities = {}

      for i in range(0, length, 2):
        quantities[content[i]] = int(content[i+1])

      numbers.append(quantities)

  return(numbers)


def getPurchaseReport():
  master = {}

  found = getPurchases()
  item_list = "Item List"

  with open("./purchases/" + item_list + ".txt") as f:
      content = f.read()
      
      content = content.split()
      content = content[3:]

      length = len(content)

      for i in range(0,length,2):
        master[content[i]] = float(content[i+1][1:])

  numbers = getNumbers(found)

  i = 0

  final = {}

  for item in found:
    final[int(item)] = calculateCost(numbers[i], master)
    i += 1

  return(final)


def calculateCost(values, master):

  cost = 0

  for key in values:
    cost += master[key] * values[key]

  cost = round(cost, 2)
  return(cost)


def getTotalSold():
  found = getPurchases()
  found = getNumbers(found)

  dict = {}

  length = len(found)

  for i in range(length):
    for key in found[i]:
      try:
        dict[key] += found[i][key]
      except:
        dict[key] = found[i][key]

  return(dict)

### TESTING PURPOSES ###

if __name__ == "__main__":
  file_list = createStructure()
  dict = getWordFrequency(file_list)
  frequency = getDuplicates(file_list)
  print(frequency)
  costs = getPurchaseReport()
  totals = getTotalSold()
