def check_password(func):
    check_log = False
    def decorated_func(*args, **kwargs):
        nonlocal check_log
        if check_log == False:
            password = input()
            if password != '123456':
                print('В доступе отказано')
                return None
        check_log = True
        return func(*args, **kwargs)
    return decorated_func

@check_password
def fibonacci(num):
    if num in (1, 2):
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(7))
