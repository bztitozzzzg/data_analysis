import numpy as np
import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [2, 4, 6]
x2 = [1, 2, 3]
y2 = [6, 2, 4]

fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x2, y2)
plt.show()

print(end='\n')


x = np.arange(0, 100, 1)
y = np.arange(0, 20, 0.2)
yy = y*y

fig, ax = plt.subplots()
ax.plot(x, yy)
plt.show()

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
