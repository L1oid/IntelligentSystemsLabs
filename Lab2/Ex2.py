a = input()
b = len(a) - int(len(a) / 2)
print(a[b:] + a[:b])