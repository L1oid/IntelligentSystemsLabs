a = int(input())
b = int(input())
c = input()
for i in range(a):
    print(c, end="")
print()
for j in range(b - 2):
    for k in range(a):
        if k == 0:
            print(c, end="")
        elif k == a - 1:
            print(c, end="")
        else:
            print(" ", end="")
    print()
for k in range(a):
    print(c, end="")