class ReversedList:
    def __init__(self, _list):
        self._list = _list[::-1]

    def __len__(self):
        return len(self._list)

    def __getitem__(self, item):
        return self._list[item]

    def __str__(self):
        return str(self._list)

a = [1, 2, 3]
r1 = ReversedList(a)
a.append(10)
for i in range(len(r1)):
    print(r1[i])
