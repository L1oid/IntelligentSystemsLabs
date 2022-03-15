access_rights = {'write': 'W', 'read': 'R', 'execute': 'X'}
file_rights = {}
for i in range(int(input())):
    file, *rights = input().split()
    file_rights[file] = set(rights)

for i in range(int(input())):
    request, file = input().split()
    if access_rights[request] in file_rights[file]:
        print("Ok")
    else:
        print("Access denied")
