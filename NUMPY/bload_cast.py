import numpy as np
a = np.arange(3)
print("a:", a)

print("a:", a+10, end='\n')

b = np.arange(-3, 3).reshape((2, 3))

print("a + b:", a + b)

a1 = a[:, np.newaxis]
print("a + a1:", a + a1)

c = np.arange(1, 7).reshape((2, 3))

print("c - np.mean(c):", c - np.mean(c))

print("b * 2:", b * 2)
print("b ** 3:", b ** 3)
print("b - a:", b - a)
print("a * b:", a * b)
print("a / c:", a / c)
print("c / a:", c / a)
print("c / (a + 1e - 6):", c / (a + 1e-6))
