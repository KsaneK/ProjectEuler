class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)

def area(p1, p2, p3):
    return abs((p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2.0)

zero = Point(0, 0)

def isInside(t):
    A = area(t.p1, t.p2, t.p3)
    A1 = area(zero, t.p2, t.p3)
    A2 = area(t.p1, zero, t.p3)
    A3 = area(t.p1, t.p2, zero)
    return A == A1 + A2 + A3

with open('p102_triangles.txt') as f:
    x = f.read().split("\n")
    if x[-1] == '':
        x = x[:-2]
    triangles = tuple(map(lambda x: Triangle(*x), (tuple(map(int, i.split(","))) for i in x)))

triangles = tuple(filter(isInside, triangles))

print(len(triangles))

