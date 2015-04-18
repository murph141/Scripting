import re, os, sys

def functions(file):
  regex = re.compile('def(\s)*(?P<functionname>[a-zA-Z][\w-]+)(\s)*\((?P<args>[\s\w,=-]+)\):')

  if(not os.path.isfile(file)):
    print('Error: File "{:s}" does not exist'.format(file))

  if(not os.access(file, os.R_OK)):
    print("Could not read {:s}".format(file))


  with open(file) as f:

    for line in f:
      a = re.match(regex, line)
      if(a):

        b = a.group("args").split(',')

        print(a.group("functionname"))
        for i in range(len(b)):
          c = b[i].strip()
          j = i + 1
          print("Arg" + str(j) + ": " + c)


if __name__ == "__main__":

  if(len(sys.argv) != 2):
    print("Usage: function_finder.py")
    quit()

  file = sys.argv[1]
  functions(file)
