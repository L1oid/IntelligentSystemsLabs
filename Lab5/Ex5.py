def palindrome(s_p):
    temp = s_p.split()
    temp = ''.join(temp)
    if temp == temp[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"
s = input()
print(palindrome(s))
