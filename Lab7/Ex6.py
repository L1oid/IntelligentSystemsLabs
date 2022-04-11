class SparseArray:
    def __init__(self):
        self.arr = dict()

    def __getitem__(self, item):
        if str(item) in self.arr:
            return self.arr[str(item)]
        return 0

    def __setitem__(self, key, value):
        if str(key) in self.arr:
            self.arr[str(key)] = value
        else:
            self.arr.update({str(key): value})

arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))