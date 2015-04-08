#!/usr/bin/env python3.4

import traceback
import sys
import vtools

if __name__ == "__main__":
  if(len(sys.argv) > 3):
    sys.exit(1)

  if(len(sys.argv) == 3):
    infile = sys.argv[1]
    outfile = sys.argv[2]
  elif(len(sys.argv) == 2):
    infile = sys.argv[1]

  try:
    in_f = open(infile, "r")
  except IOError as e:
    print("Error: {}".format(e))
    sys.exit(2)

  if(len(sys.argv) == 3):
    try:
      out_f = open(outfile, "w")
    except IOError as e:
      print("Error: {}".format(e))
      sys.exit(3)
  else:
    out_f = sys.stdout

  content = []
  for line in in_f:
    content.append(line.strip())

  for item in content:
    new_net = list(vtools.parse_net(item))

    if(len(new_net) == 0):
      print("Error: input file is not a valid Verilog port map!")
      sys.exit(4)

    print("{0}: {1} PORT MAP(".format(new_net[1], new_net[0]))

    the_new_net = new_net[2:]

    for i in range(0,len(the_new_net) - 1, 2):
      print("{0}=>{1}".format(the_new_net[i], the_new_net[i+1]))

      if(i + 2 < len(the_new_net)):
        print(", ")
      else:
        print(")")
