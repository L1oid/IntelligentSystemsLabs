def alphabet():
    for i in range(1072, 1078):
        yield chr(i)
    yield chr(1105)
    for i in range(1078, 1104):
        yield chr(i)

print(*alphabet())
