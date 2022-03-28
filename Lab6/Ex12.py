str_ = input().split()
print(*sorted(str_, key=lambda s: s.lower()))
