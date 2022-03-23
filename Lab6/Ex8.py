from itertools import chain

alphabet = (chr(i) for i in chain(range(1072, 1078), iter([1105]), range(1078, 1104)))
print(*alphabet)
