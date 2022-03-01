numbers = [4, 2, 5, 5, 4, 3]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            break
    else:
        print(numbers[i], end = ' ')
