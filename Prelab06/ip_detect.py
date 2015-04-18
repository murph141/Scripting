import re

def getIPs():
  regex = re.compile('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')

  with open("addys.in") as f:

    for line in f:

      test = 0

      line = line.rstrip()
      a = line.split(':')

      ip = a[0]
      try:
        port = int(a[1])
      except:
        port = a[1]
        test = 1

      print(ip + ":" + str(port), end="")

      if test:
        port = 0

      a = re.findall(regex, ip)

      ip = ip.split('.')

      for item in a:
        a = item

      try:
        new_ip = (ip[0], ip[1], ip[2], ip[3])
      except:
        pass

      if(a == new_ip):

        if(port > 32767 or port < 1):
          print(" - Invalid Port Number")
        else:
          print(" -  Valid ", end="")

          if(port < 1024):
            print("(root privledges required)")
          else:
            print()

      else:
        print(" - Invalid IP Address")


if __name__ == "__main__":
  getIPs()
