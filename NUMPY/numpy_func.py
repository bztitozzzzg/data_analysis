import numpy as np

a = np.arange(3)
b = np.arange(-3, 3).reshape((2, 3))
c = np.arange(1, 7).reshape((2, 3))
d = np.arange(6).reshape((3, 2))
e = np.linspace(-1, 1, 10)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)

print(end='\n')

print("a:", a.shape)
print("b:", b.shape)
print("c:", c.shape)
print("d:", d.shape)
print("e:", e.shape)
