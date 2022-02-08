a = int(input())
for i in range(a):
    if i == 0:
        print((a - 1) * " " + "*")
        b = 3
    else:
        print((a - (i + 1)) * " " + b * "*")
        b = b + 2