numbers = [1, 2, 23, 6, 4, 1, 55]

filter_numbers = list(map(lambda number: number / 2, numbers))
print(*filter_numbers)

filter_numbers = [number / 2 for number in numbers]
print(*filter_numbers)
