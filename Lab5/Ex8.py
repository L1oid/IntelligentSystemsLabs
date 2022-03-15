def mirror(arr):
    mirrored_part = reversed(arr)
    arr += list(mirrored_part)

arr = [1, 2]
mirror(arr)
print(*arr)
