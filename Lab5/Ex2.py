from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(distance(a, b, c, d))
