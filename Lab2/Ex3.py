a = input()
str1 = a[:a.find('h') + 1]
str2 = a[a.find('h') + 1:a.rfind('h')]
str3 = a[a.rfind('h'):]
print(str1 + str2[::-1] + str3)