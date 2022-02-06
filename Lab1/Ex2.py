a = input()
b = input()
if ((a == 'Да' and b == 'Да') or (a == 'Нет' and b == 'Нет') or (a == 'Да' and b == 'Нет') or (a == 'Нет' and b == 'Да')):
    print('Верно')
else:
    print('Неверно')