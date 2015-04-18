import re

def substitute():
  regex1 = re.compile('(?P<user>[\w-]+)@purdue.edu(\s)*')
  regex2 = re.compile('(\d)+.(\d)+')

  emails = []
  scores = []

  with open("Part2.in") as f:

    for line in f:
      line = line.split()

      a = re.match(regex1, line[0])

      if(re.match(regex1, line[0])):
        emails.append(a.group("user") + "@ecn.purdue.edu")
        a = re.match(regex2, line[1]).group()
        a += "/100"
        scores.append(a)

  for j in range(len(emails)):
    print(emails[j] + "\t" + scores[j])


if __name__ == "__main__":
  substitute()
