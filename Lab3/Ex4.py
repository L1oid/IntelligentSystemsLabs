numbers = ['12', '23', '24', '23']
check = set()
for i in numbers:
    if i in check:
        print('Yes')
    else:
        print('No')
        check.add(i)