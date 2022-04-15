import numpy as np

print("a)")
arr_1 = np.ndarray((3, 4), dtype=int)
arr_1.fill(3)
print(arr_1)

print("b)")
arr_2 = np.random.randint(0, 9, size=(2, 4))
print(arr_2)

print("c)")
print(arr_1.size)
print(arr_2.size)

print("d)")
print(np.concatenate((arr_1, arr_2), 0))

print("e)")
arr_3 = np.array([1, 8, 6, 5, 8, 3])
print(arr_3)

print("f)")


