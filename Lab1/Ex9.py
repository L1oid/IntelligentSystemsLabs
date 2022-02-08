a = input()
b = input()
check = 0
while check == 0:
    if len(a) < 8:
        check = 0
        print("Короткий!")
        a = input()
        b = input()
    elif "123" in a:
        check = 0
        print("Простой!")
        a = input()
        b = input()
    elif a != b:
        check = 0
        print("Различаются!")
        a = input()
        b = input()
    else:
        check = 1
        print("ОК")