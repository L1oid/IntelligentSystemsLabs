def factorials(n):
    def factorial(num):
        if num == 0:
            return 1
        return factorial(num - 1) * num
    for i in range(1, n + 1):
        yield factorial(i)

print(*factorials(int(input())))
