num = int(input())
c = int(num % 10)
b = int((num % 100) / 10)
a = int(num / 100)
if a > c:
    a, c = c, a
if a > b:
    a, b = b, a
if c < b:
    c, b = b, c
if (a + c) / 2 == b:
    print("Красивое!")
else:
    print("Обычное!")