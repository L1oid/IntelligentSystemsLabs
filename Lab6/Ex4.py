numbers = [18, 19, 20, 5, 33, 6, 1]

filter_numbers = list(map(lambda number: number / 2, filter(lambda number: number > 17, numbers)))
print(*filter_numbers)

filter_numbers = [number / 2 for number in numbers if number > 17]
print(*filter_numbers)
