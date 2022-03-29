def cached(func):
    cache = {}
    def decorated_func(*args, **kwargs):
        nonlocal cache
        if not cache.get(args):
            result = func(*args, **kwargs)
            cache[args] = result
        return cache[args]
    return decorated_func

@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(7))
print(fib(7))