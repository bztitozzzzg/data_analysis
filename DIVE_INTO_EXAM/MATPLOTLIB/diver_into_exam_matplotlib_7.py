import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
x1 = np.random.normal(0, 10, 1000)
x2 = np.random.normal(0, 15, 1000)
x3 = np.random.normal(0, 20, 1000)

fig, ax = plt.subplots()
labels = ['x1', 'x2', 'x3']
ax.boxplot((x1, x2, x3), labels=labels)
plt.show()

print(end='\n')

fig, ax = plt.subplots()
ax.boxplot((x1, x2, x3), labels=labels, vert=False)
plt.show()

print(end='\n')
print('*************************', end='\n')
print('******確認試験******', end='\n')
np.random.seed(123)
x1 = np.random.normal(0, 10, 1000)
x2 = np.random.normal(0, 15, 1000)
x3 = np.random.normal(0, 20, 1000)
fig, ax = plt.subplots()
# 横に描画するには引数に vert=False
ax.boxplot((x1, x2, x3), labels=labels, vert=False)
plt.show()
