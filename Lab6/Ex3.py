sum_numbers = sum(map(lambda number: number ** 2, filter(lambda number: number % 9 == 0, range(10, 100))))
print(sum_numbers)
