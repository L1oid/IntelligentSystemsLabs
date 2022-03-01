numbers = [2, -4, 5, -6]
for i in range(1, len(numbers)):
    if numbers[i - 1] * numbers[i] > 0:
        print(numbers[i - 1], numbers[i])
        break
