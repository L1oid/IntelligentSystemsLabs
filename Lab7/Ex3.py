class Selector:
    def __init__(self, values_p):
        self.values = values_p

    def get_odds(self):
        for num in self.values:
            if num % 2 != 0:
                yield num
    def get_evens(self):
        for num in self.values:
            if num % 2 == 0:
                yield num

values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))