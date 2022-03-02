check = dict()
for word in input().split():
    if word in check:
        check[word] = check.get(word) + 1
        print(check.get(word))
    else:
        check[word] = 0
        print(check.get(word))
