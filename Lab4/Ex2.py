count = int(input())
synonyms = dict(input().split() for i in range(count))
word = input()
if word in synonyms.keys():
    print(synonyms[word])
else:
    for key, values in synonyms.items():
        if values == word:
            print(key)
