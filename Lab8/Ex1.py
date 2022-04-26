import numpy as np

arr_1 = np.ndarray((3, 4), dtype=int)
arr_1.fill(3)
print(arr_1)

arr_2 = np.random.randint(0, 9, size=(2, 4))
print(arr_2)

print(arr_1.size)
print(arr_2.size)

print(np.concatenate((arr_1, arr_2), 0))

arr_3 = np.array([1, 8, 6, 5, 8, 3])
print(arr_3)

arr_3 *= 3
arr_3 += 1

arr_4 = arr_3.copy()

arr_3 = arr_3.reshape((2, 3))
arr_5 = arr_3.copy()

print(arr_4)
print(arr_5)
print(np.min(arr_5, axis=1))
print(np.average(arr_5))

arr_6 = np.ndarray((11, 1), dtype=int)
for i in range(11):
    arr_6.put(i, i ** 2)

print(arr_6[1::2])
print(arr_6[::-1])

for i in range(1, 11, 2):
    arr_6.put(i, 2)
print(49 in arr_6)

A = np.random.randint(-10, 10, size=(5, 5))
print(A)

B = A[A < 0]
print(B)