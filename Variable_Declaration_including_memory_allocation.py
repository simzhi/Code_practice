#Variable Declaration including memory allocation & type casting:
#Write a Python function that takes two integers as input and allocates memory for a 2D
#array of size m x n. Implement type casting to convert the input integers to
#appropriate data types.

import numpy as np
def allocates(m, n):
    arr = np.zeros((m, n), dtype=np.int32)
    return arr

print(allocates(3,4))
