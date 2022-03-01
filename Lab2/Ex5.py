numbers = ['2', '4', '5', '6']
for i in range(len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i])