from math import sqrt

def power(a, n):
    b = 1
    for i in range(abs(n)):
        b *= a
    if n >= 0:
        return b
    else:
        return 1 / b
n1 = float(input())
n2 = int(input())
print(power(n1, n2))
