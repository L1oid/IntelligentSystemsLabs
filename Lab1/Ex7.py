num = int(input())
a = int(num % 10)
b = int((num % 100) / 10)
c = int((num / 100) % 10)
d = int(num / 1000)
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(str(a) + str(b) + str(c) + str(d))