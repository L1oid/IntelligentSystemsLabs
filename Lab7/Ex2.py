class Balance:
    def __init__(self):
        self.right_weight = 0
        self.left_weight = 0

    def add_right(self, weight):
        self.right_weight += weight

    def add_left(self, weight):
        self.left_weight += weight

    def result(self):
        if self.right_weight == self.left_weight:
            return "="
        elif self.right_weight > self.left_weight:
            return "R"
        elif self.right_weight < self.left_weight:
            return "L"

balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())
