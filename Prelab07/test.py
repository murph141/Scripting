#!/usr/bin/env python3.4

import math

class Point2D:
  def __init__(self, x=0.0, y=0.0):
    self.x = float(x)
    self.y = float(y)

  def dist_between(self, other):
    xsq = (self.x - other.x) * (self.x - other.x)
    ysq = (self.y - other.y) * (self.y - other.y)
    return math.sqrt(xsq + ysq)

  def __str__(self):
    return("({}, {})".format(self.x, self.y))


class MyPoint2D(Point2D):
  def __init__(self, x=0.0, y=0.0):
    Point2D.__init__(self, x, y)

  def get_max_coord(self):
    return(self.y if self.x < self.y else self.x)

  def get_min_coord(self):
    return(self.x if self.x < self.y else self.y)


if __name__ == "__main__":
  list = []

  for i in range(1,11,1):
    for j in range(1,11,1):
      pt = Point2D(i, j)
      list.append(pt)

  pt = Point2D(3.14, 2.72)
  print(pt)

  mpt = MyPoint2D(7, 4)
  print(mpt.get_max_coord())
  print(mpt.get_min_coord())
