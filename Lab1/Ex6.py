num = int(input())
c = int(num % 10)
b = int((num % 100) / 10)
a = int(num / 100)
if a > c:
    temp = a
    a = c
    c = temp
if a > b:
    temp = a
    a = b
    b = temp
if c < b:
    temp = c
    c = b
    b = temp
if (a + c) / 2 == b:
    print("Красивое!")
else:
    print("Обычное!")