#!/usr/bin/env python3.4

class Entry:
  def __init__(self, k=0, v=''):
    if(type(k) is not int):
      raise ValueError("k must be of type int")
    
    if(type(v) is not str):
      raise ValueError("v must be of type str")

    self.key = k
    self.value = v

  def __str__(self):
    return("({0}: {1})".format(self.key, str(self.value)))

  def __hash__(self):
    t = (self.key, self.value)
    return(hash(t))


class Lookup:
  def __init__(self, name):
    if(name is ""):
      raise ValueError("name must not be empty")

    self._name = name
    self._entrySet = set()

  def __str__(self):
    return('["{0}": {1:02d} Entries]'.format(self._name, len(self._entrySet)))

  def addEntry(self, entry):
    for item in self._entrySet:
      if(item == entry):
        raise ValueError("Entry already present")

    self._entrySet.add(entry)

  def updateEntry(self, entry):
    remove = 0
    to_remove = ""
    for item in self._entrySet:
      item2 = str(item)[1:]
      the_key = int(item2.split(':')[0])

      item3 = str(entry)[1:]
      the_key2 = int(item3.split(':')[0])

      if(the_key == the_key2):
        remove = 1
        to_remove = item

    if(remove == 0):
      raise KeyError("Entry is not present")
    else:
      self._entrySet.remove(to_remove)
      self._entrySet.add(entry)

  def addOrUpdateEntry(self, entry):
    for item in self._entrySet:
      item2 = str(item)[1:]
      the_key = int(item2.split(':')[0])

      item3 = str(entry)[1:]
      the_key2 = int(item3.split(':')[0])

      if(the_key == the_key2):
        found = 1

    if(found == 1):
      self.updateEntry(entry)
    else:
      self.addEntry(entry)

  def removeEntry(self, entry):
    remove = 0
    to_remove = ""
    for item in self._entrySet:
      item2 = str(item)[1:]
      the_key = int(item2.split(':')[0])

      item3 = str(entry)[1:]
      the_key2 = int(item3.split(':')[0])

      if(the_key == the_key2):
        remove = 1
        to_remove = item

    if(remove == 0):
      raise KeyError("Entry is not present")
    else:
      self._entrySet.remove(to_remove)

  def getEntry(self, key):
    for item in self._entrySet:
      item2 = str(item)[1:]
      the_key = int(item2.split(':')[0])

      if(key == the_key):
        return(item)

    raise KeyError("Key is not present")

  def addOrUpdateFromDictionary(self, someDict):
    for key, value in someDict.items():

      for item in self._entrySet:
        item2 = str(item)[1:]
        the_key = int(item2.split(':')[0])

        if(key == the_key):
          self.updateEntry(Entry(key, str(value)))
        else:
          self.addEntry(Entry(key, str(value)))

      if(len(self._entrySet) == 0):
        self.addEntry(Entry(key, str(value)))
  
  def getAsDictionary(self):
    a = {}

    for item in self._entrySet:
      item2 = str(item)[1:].split(':')
      key = int(item2[0])
      value = item2[1][1:-1]

      a[key] = value

    return(a)

  def getKeys(self):
    master = []

    for item in self._entrySet:
      item2 = str(item)[1:].split(':')
      key = int(item2[0])

      master.append(key)
    
    master.sort()

    return(master)

  def getValues(self):
    master = []

    for item in self._entrySet:
      item2 = str(item)[1:].split(':')
      value = item2[1][1:-1]

      master.append(value)

    master.sort()

    return(master)

  def getElementCount(self):
    return(len(self._entrySet))

if __name__ == "__main__":
  a = Entry(42, 'The answer to life')
  c = Entry(42, 'answer to life')
  print(a)

  b = Lookup("adsfsa")
  print(b)
  b.addEntry(a)
  print(b)
  b.addOrUpdateEntry(c)
  print(b)
  print(b.getEntry(42))
  b.removeEntry(a)
  print(b)

  f = {}
  f[16] = 'hey'

  b.addOrUpdateFromDictionary(f)
  print(b)
  print(b.getEntry(16))
  print(b.getAsDictionary())
  b.addEntry(a)
  print(b.getKeys())
  print(b.getValues())
