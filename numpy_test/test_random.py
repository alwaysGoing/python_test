import random
import math

# set the seed of random
random.seed(0)

a = random.randrange(0, 10, 4)  # random.randrange(start, stop[, step])
print(a)

a = random.randint(2, 4)  # random.randint(a, b), Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
print(a)

a = random.random()
print(a)