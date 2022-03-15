count_v = dict()
for i in range(int(input())):
    candidate, votes = input().split()
    count_v[candidate] = count_v.get(candidate, 0) + int(votes)
for candidate, votes in sorted(count_v.items()):
    print(candidate, votes)
