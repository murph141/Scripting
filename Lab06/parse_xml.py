#!/usr/bin/env python3.4

import re

def convertToAttrib():
  regex = r"<point>.*?</point>"
  regex2 = r"<ID>(?P<id>.*?)</ID>"
  regex3 = r"<X>(?P<X>.*?)</X>"
  regex4 = r"<Y>(?P<Y>.*?)</Y>"

  big_string = ""
  with open("points.xml") as f:

    for line in f:
      big_string += line

  b = []
  a = re.findall(regex, big_string, re.S)

  for item in a:
    b.append(item.strip())

  c = []
  for item in b:
    d = []
    point = re.search(regex2, item, re.S)
    point = point.group("id").strip()

    X = re.search(regex3, item, re.S)
    X = X.group("X").strip()

    Y = re.search(regex4, item, re.S)
    Y = Y.group("Y").strip()
    d.append(point)
    d.append(X)
    d.append(Y)
    c.append(d)

  with open("points_out.xml", "w") as f:
    f.write('<?xml version="1.0"?>\n')
    f.write('<coordinates>\n')

    for item in c:
      f.write('   <point ID="' + item[0] + '" X="' + item[1] + '" Y="' + item[2] + '" />\n')

    f.write('</coordinates>\n')


def getGenres():
  regex = re.compile("<genre>(?P<genre>.*?)</genre>")

  genres = []

  with open("books.xml") as f:
    
    for line in f:
      if(regex.search(line)):
        a = regex.search(line)
        genre = a.group("genre")

        if genre not in genres:
          genres.append(genre)

  genres.sort()

  return(genres)

def getAuthorOf(bookname):
  regex = re.compile("<author>(?P<author>.*?)</author>\n.*?<title>" + bookname + "</title>")

  big_string = ""
  with open("books.xml") as f:

    for line in f:
      big_string += line

  a = regex.findall(big_string)

  if(len(a)):
    return(a[0])
  else:
    return(None)


def getBookInfo(bookID):
  regex = re.compile('<book id="' + bookID + '">\n.*?<author>(?P<author>.*?)</author>\n.*?<title>(?P<title>.*?)</title>')

  big_string = ""
  with open("books.xml") as f:

    for line in f:
      big_string += line

  a = regex.findall(big_string)

  if(len(a)):
    x, y = a[0]
    return(y, x)
  else:
    return(None)


def getBooksBy(authorName):
  regex = re.compile("<author>" + authorName + "</author>\n.*?<title>(?P<book>.*?)</title>")

  books = []
  big_string = ""
  with open("books.xml") as f:

    for line in f:
      big_string += line

  a = regex.findall(big_string)

  if(len(a)):
    return(a)
  else:
    return(None)


def getBooksBelow(bookPrice):
  regex = re.compile("<title>(?P<title>.*?)</title>.*?\n.*?\n.*?<price>(?P<book_price>.*?)</price>")

  books = []
  big_string = ""
  with open("books.xml") as f:

    for line in f:
      big_string += line

  a = regex.findall(big_string)

  for item in a:
    book, price = item

    if(float(price) < bookPrice):
      books.append(book)

  return(books)
  

def searchForWord(word):
  regex = r"<title>(?P<title>.*?)</title>.*?<description>(?P<desc>.*?)</description>"
  regex2 = r"\s" + word

  books = []
  big_string = ""
  with open("books.xml") as f:

    for line in f:
      big_string += line

  a = re.findall(regex, big_string, re.S)
  
  for item in a:
    if(word in item[0]):
      books.append(item[0])
    elif(re.search(regex2, item[1], re.S)):
      books.append(item[0])

  return(books)


if __name__ == "__main__":
  print(searchForWord("the"))
