def square_fibonacci(n):
    def fibonacci(num):
        if num in (1, 2):
            return 1
        return fibonacci(num - 1) + fibonacci(num - 2)
    for i in range(1, n + 1):
        yield fibonacci(i) ** 2

print(*square_fibonacci(int(input())))
