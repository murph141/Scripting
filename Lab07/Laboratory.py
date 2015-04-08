#!/usr/bin/env python3.4

import copy as c
import string

class Experiment:
  def __init__(self, experimentNo, experimentDate, virusName, unitCount, unitCost):
    self.experimentNo = experimentNo
    self.experimentDate = experimentDate
    self.virusName = virusName
    self.unitCount = unitCount
    self.unitCost = unitCost
    self.totalCost = float(unitCost) * float(unitCount)

  def __str__(self):
    return("{0:03d}, {1}, ${2:06.2f}: {3}".format(self.experimentNo, self.experimentDate, self.totalCost, self.virusName))

class Technician:
  def __init__(self, techName, techID):
    self.techName = techName
    self.techID = techID
    self.experiments = {}

  def addExperiment(self, experiment):
    self.experiments[experiment.experimentNo] = c.deepcopy(experiment)

  def __str__(self):
    num = len(self.experiments)
    a = "s" if num != 1 else ""
    return("{0}, {1}: {2:02d} Experiment{3}".format(self.techID, self.techName, num, a))

  def generateTechActivity(self):
    string = "{0}, {1}\n".format(self.techID, self.techName)

    empty = []
    for value in self.experiments.values():
      empty.append(value)

    for i in range(len(empty)):
      for j in range(i, len(empty)):
        a = int(empty[i].experimentNo)
        b = int(empty[j].experimentNo)

        if(b < a):
          empty[i], empty[j] = empty[j], empty[i]

    for item in empty:
      string += str(item) + '\n'

    return(string)

  def loadExperimentsFromFile(self, fileName):
    a = []

    with open(fileName, 'r') as f:
      f.readline()
      f.readline()
      content = f.read()
      content = content.split()

      a = [content[5*x:5*(x+1)] for x in range(int(len(content)/5))]
      
    for item in a:
      e0 = Experiment(int(item[0]), item[1], item[2], int(item[3]), float(item[4][1:]))
      self.addExperiment(e0)


class Laboratory:
  def __init__(self, labName):
    self.labName = labName
    self.technicians = {}

  def addTechnician(self, technician):
    self.technicians[technician.techName] = c.deepcopy(technician)

  def __str__(self):
    num = len(self.technicians)
    a = "s" if num != 1 else ""
    string = "{0}: {1:02d} Technician{2}\n".format(self.labName, num, a)
        
    empty = []
    for value in self.technicians.values():
      empty.append(value)

    for i in range(len(empty)):
      for j in range(i, len(empty)):
        a = empty[i].techID[0:5] + empty[i].techID[6:]
        b = empty[j].techID[0:5] + empty[j].techID[6:]
        a = int(a)
        b = int(b)
        if(b < a):
          empty[i], empty[j] = empty[j], empty[i]

    for item in empty:
      string += str(item) + '\n'

    return(string[0:-1])

  def generateLabActivity(self):
    string = ""

    empty = []
    for values in self.technicians.values():
      empty.append(values)

    for i in range(len(empty)):
      for j in range(i, len(empty)):
        a = empty[i].techName.lower()
        b = empty[j].techName.lower()
        if(b < a):
          empty[i], empty[j] = empty[j], empty[i]

    for item in empty:
      string += str(item.generateTechActivity()) + '\n'

    return(string[0:-1])

if __name__ == "__main__":
  t0 = Technician("John", "00260-00256")
  t1 = Technician("Eric", "11111-22222")
  e0 = Experiment(5, "5/5/2015", "Bill Virus", 5, 7.75)
  e1 = Experiment(6, "5/5/2015", "Bill Virus", 5, 7.75)
  e2 = Experiment(55, "10/11/2012", "New Virus", 2, 2)
  t0.addExperiment(e0)
  t0.addExperiment(e1)
  t1.addExperiment(e1)
  t1.addExperiment(e2)

  print(t0.generateTechActivity())

  t0.loadExperimentsFromFile('report 55926-36619.txt')

  l0 = Laboratory("Eli Lilly")
  l0.addTechnician(t0)
  l0.addTechnician(t1)
  print(l0)
  print(l0.generateLabActivity())
