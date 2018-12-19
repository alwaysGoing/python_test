import random
import math
import numpy as np

# set the seed of random
random.seed(0)
np.random.seed(0)

a = random.randrange(0, 10, 4)  # random.randrange(start, stop[, step])
print(a)

a = random.randint(2, 4)  # random.randint(a, b), Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
print(a)

a = random.random()
print(a)

a = np.random.random(3)
print(a)

a = np.random.random()
print(a)

a = np.random.rand(3, 4)  # rand(d0, d1, …, dn), Random values in a given shape.
print(a)

a = np.random.randn(4, 5)  # randn(d0, d1, …, dn), Return a sample (or samples) from the “standard normal” distribution.
print(a)

a = np.random.randint(3, 5) # randint(low[, high, size, dtype]), Return random integers from low (inclusive) to high (exclusive).
print(a)