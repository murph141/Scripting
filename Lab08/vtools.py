#!/usr/bin/env python3.4

import string
import re

def is_valid_name(ID):
  for item in ID:
    if(item not in string.ascii_letters and item not in "1234567890" and item not in "_"):
      return(False)

  return (True)

def parse_pin_assignment(assignment):
  if(assignment[0] != '.' or assignment[-1] != ')' or '(' not in assignment):
    raise ValueError(assignment)

  assign = assignment[1:]
  assign = assign.split('(')
  assign[1] = assign[1][:-1]

  if(not is_valid_name(assign[0]) or not is_valid_name(assign[1]) or len(assign) != 2):
    raise ValueError(assignment)

  return(assign[0], assign[1])

  
def parse_net(line):
  regex = r"\s*(?P<component>\w+)\s+(?P<instance>\w+)\s*\((?P<outside>.*)\)\s*"

  a = re.match(regex, line)

  component = a.group("component")
  instance = a.group("instance")
  outside = a.group("outside")

  outside = outside.split(',')

  master = []
  for item in outside:
    item = item.strip()
    tup = parse_pin_assignment(item)
    master.append(tup)

  return((component, instance, tuple(master)))


if __name__ == "__main__":
  pass
