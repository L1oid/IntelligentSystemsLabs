count = int(input())
words = set()
for i in range(count):
    words.update(input().split())
print(len(words))
