import numpy as np


def make_field(size):
    v = np.arange(size) % 2
    m = np.meshgrid(v, v)
    return np.int8(m[0] != m[1])


print(make_field(int(input())))
