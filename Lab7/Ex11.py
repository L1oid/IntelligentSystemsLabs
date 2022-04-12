class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        count = 0
        for i in range(n + 1):
            count += self.transform(int(i))
        return count


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 2


class CubeSummator(PowerSummator):
    def __init__(self):
        pass

    def transform(self, n):
        return n ** 3


s = Summator()
print(s.transform(5))
print(s.sum(5))
print('---------------')

s = SquareSummator()
print(s.transform(5))
print(s.sum(5))
print('---------------')

s = CubeSummator()
print(s.transform(5))
print(s.sum(5))
print('---------------')

s = PowerSummator(4)
print(s.transform(3))
print(s.sum(3))
