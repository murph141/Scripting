import sys

if __name__ == "__main__":
  if(len(sys.argv) != 2):
    print("Usage: parse.py [filename]")
    sys.exit(1)

  file = sys.argv[1]

  try:
    f = open(file)
  except IOError:
    print("{} is not a readable file.".format(file))
    sys.exit(1)

  big_list = []
  for line in f:
    big_list.append(line.rstrip())

  for item in big_list:
    sum = 0
    total = 0
    string = ""
    item = item.split(' ')

    for value in item:
      try:
        sum += float(value)
        total += 1
      except ValueError:
        string += value + " "

    if(not sum):
      print(string[:-1])
    else:
      print("{0:0.3f} ".format(sum / total) + string[:-1])
