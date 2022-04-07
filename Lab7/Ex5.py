class ReversedList:
    def __init__(self, values):
        self.values = values[::-1]

    def

a = [1, 2, 3]
r1 = ReversedList(a)
a.append(10)
for i in range(len(r1)):
    print(r1[i])