#!/usr/bin/env python3.4

import math

class Point3D:
  def __init__(self, x=0.0, y=0.0, z=0.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  def __str__(self):
    return("({x:.2f}, {y:.2f}, {z:.2f})".format(x=self.x, y=self.y, z=self.z))

  def distFrom(self, other):
    xsq = (self.x - other.x) * (self.x - other.x)
    ysq = (self.y - other.y) * (self.y - other.y)
    zsq = (self.z - other.z) * (self.z - other.z)

    return(math.sqrt(xsq + ysq + zsq))

  def __hash__(self):
    tuple = self.x, self.y, self.z
    return(hash(tuple))

  def nearestPoint(self, points):
    if(len(points) == 0):
      return(None)

    dist = self.distFrom(points[0])
    point = points[0]

    for item in points:
      d = self.distFrom(item)

      if(d < dist):
        dist = d
        point = item

    return(point)

  def clone(self):
    return(self)

  def __add__(self, other):
    if isinstance(other, Point3D):
      return(Point3D(self.x + other.x, self.y + other.y, self.z + other.z))
      
    return(Point3D(self.x + other, self.y + other, self.z + other))

  __radd__ = __add__

  def __sub__(self, other):
    if isinstance(other, Point3D):
      return(Point3D(self.x - other.x, self.y - other.y, self.z - other.z))
      
    return(Point3D(self.x - other, self.y - other, self.z - other))

  def __neg__(self):
    return(Point3D(-self.x, -self.y, -self.z))

  def __truediv__(self,  other):
    return(Point3D(self.x / other, self.y / other, self.z / other))

  def __mul__(self, other):
    return(Point3D(self.x * other, self.y * other, self.z * other))

  __rmul__ = __mul__

  def __eq__(self, other):
    if not isinstance(other, Point3D):
      return(False)

    return(self.x == other.x and self.y == other.y and self.z == other.z)

  def __gt__(self, other):
    if not isinstance(other, Point3D):
      return(False)

    origin = Point3D()
    return(self.distFrom(origin) > other.distFrom(origin))

  def __ge__(self, other):
    if not isinstance(other, Point3D):
      return(False)

    origin = Point3D()
    return(self.distFrom(origin) >= other.distFrom(origin))

  def __lt__(self, other):
    if not isinstance(other, Point3D):
      return(False)

    origin = Point3D()
    return(self.distFrom(origin) < other.distFrom(origin))

  def __le__(self, other):
    if not isinstance(other, Point3D):
      return(False)

    origin = Point3D()
    return(self.distFrom(origin) <= other.distFrom(origin))


class PointSet():
  def __init__(self, points=set()):
    self.points = points

  def addPoint(self, p):
    self.points.add(p)

  def count(self):
    return(len(self.points))

  def computeBoundingBox(self):
    first = 1

    for item in self.points:
      if(first):
        first = 0
        min_x = item.x
        max_x = min_x
        min_y = item.y
        max_y = min_y
        min_z = item.z
        max_z = min_z
      else:
        x = item.x
        y = item.y
        z = item.z
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
        max_z = z if z > max_z else max_z
        min_x = x if x < min_x else min_x
        min_y = y if y < min_y else min_y
        min_z = z if z < min_z else min_z
    
    return(Point3D(x=min_x, y=min_y, z=min_z), Point3D(x=max_x, y=max_y, z=max_z))


  def computeNearestNeighbors(self, other):
    tuple_list = []
    for item in self.points:
      tuple_list.append((item, item.nearestPoint(other)))

    return(tuple_list)

  def __add__(self, other):
    if isinstance(other, Point3D):
      temp = self.points.copy()
      temp = temp.add(other)
      return(PointSet(points=temp))
    elif isinstance(other, PointSet):
      temp = self.points.copy()
      temp = temp.union(other.points)
      return(PointSet(points=temp))

  def __sub__(self, other):
    if isinstance(other, Point3D):
      temp = self.points.copy()
      temp.discard(other)
      return(PointSet(points=temp))
    elif isinstance(other, PointSet):
      temp = self.points.copy()
      temp = temp.difference(other.points)
      return(PointSet(points=temp))

  def __gt__(self, other):
    return(len(self.points) > len(other.points))

  def __ge__(self, other):
    return(len(self.points) >= len(other.points))

  def __lt__(self, other):
    return(len(self.points) < len(other.points))

  def __le__(self, other):
    return(len(self.points) <= len(other.points))

  def __str__(self):
    for item in self.points:
      print("({x:.2f}, {y:.2f}, {z:.2f})".format(x=item.x, y=item.y, z=item.z))
    return("")

if __name__ == "__main__":
  pt1 = Point3D(0, 0, -0.5)
  pt2 = Point3D(1, 3, 3)
  pt3 = Point3D(1, 1, 3)
  pt4 = Point3D(1, 0, 0)
  pt5 = Point3D(1, 0, 1)

  l = []
  l.append(pt1)
  l.append(pt2)
  l.append(pt3)
  l.append(pt4)
  l.append(pt5)

  p1 = Point3D(0, 0, 0)
  p2 = Point3D(1, 0, 0)
  points = set()
  points.add(p1)
  points.add(p2)
  a = PointSet(points)

  p1 = Point3D(0, 1, 0)
  p2 = Point3D(1, 0, 0)
  points = set()
  points.add(p1)
  points.add(p2)
  b = PointSet(points)

  print(a)
  print(b)
  print(a + b)
  print(a - b)
  print(a - pt5)
  print(a - pt4)
