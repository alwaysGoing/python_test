import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.zeros([3, 2])
print(a)
print(b)

# delete(arr, index of where, axis)

# delete the index(1) element of axis 0 of a
c = np.delete(a, 1, 0)
print(c)

# delete operator generates a new array c, not cover the origin a used a new a.
print(a)

# delete the index(0) element of axis 1 of a
c = np.delete(a, 0, 1)
print(c)

