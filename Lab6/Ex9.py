def arithmetic_operation(operation_):
    if operation_ == '+':
        return lambda a, b: a + b
    elif operation_ == '-':
        return lambda a, b: a - b
    elif operation_ == '/':
        return lambda a, b: a / b
    elif operation_ == '*':
        return lambda a, b: a * b

operation = arithmetic_operation('*')
print(operation(2, 4))
