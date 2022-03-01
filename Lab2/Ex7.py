numbers = [2, 4, 5, 6, 4]
for i in range(1, len(numbers), 2):
    temp = numbers[i - 1]
    numbers[i - 1] = numbers[i]
    numbers[i] = temp
print(numbers)