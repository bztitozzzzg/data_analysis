import numpy as np

a = np.arange(3)
b = np.arange(-3, 3).reshape((2, 3))

print("np.dot(b, a):", np.dot(b, a))
print("b @ a:", b @ a)
"""
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0,
with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 3)
"""
#print("a : b:", a @ b)

d = np.arange(6).reshape((3, 2))

print("b @ d:", b @ d)
print("d @ b:", d @ b)
