numbers = [1, 2, 23, 6, 4, 1, 55]

filter_numbers = list(filter(lambda number: number < 5, numbers))
print(*filter_numbers)

filter_numbers = [number for number in numbers if number < 5]
print(*filter_numbers)
