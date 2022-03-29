def check_password(password_p):
    def decorated_func(func):
        check_log = False
        def decorated2_func(*args, **kwargs):
            nonlocal check_log
            if check_log == False:
                password = input()
                if password != password_p:
                    print('В доступе отказано')
                    return None
            check_log = True
            return func(*args, **kwargs)
        return decorated2_func
    return decorated_func

@check_password('123456')
def fibonacci(num):
    if num in (1, 2):
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(7))