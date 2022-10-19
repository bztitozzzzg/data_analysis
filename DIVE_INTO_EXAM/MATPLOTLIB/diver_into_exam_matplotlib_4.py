import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [4, 12, 5]
y2 = [8, 2, 4]
y_total = np.add(y1, y2)
labels = ['Apple', 'Banana', 'Orange']

ax.bar(x, y_total, tick_label=labels, label='y2')
ax.bar(x, y1, label='y1')
ax.legend()
plt.show()
"""
実行結果
"""

print(end='\n')

fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [4, 12, 5]
y2 = [8, 2, 4]
y3 = [2, 6, 8]
y1_y2_total = np.add(y1, y2)
y_total = np.add(y1_y2_total, y3)
labels = ['Apple', 'Banana', 'Orange']

ax.bar(x, y_total, tick_label=labels, label='y3')
ax.bar(x, y1_y2_total, tick_label=labels, label='y2')
ax.bar(x, y1, label='y1')
ax.legend()
plt.show()

print(end='\n')

x = [1, 2, 3]
y1 = [4, 12, 5]
y2 = [8, 2, 14]
y3 = [10, 6, 8]
y1_y2_total = [num1 + num2 for num1, num2 in zip(y1, y2)]
y_total = [num1 + num2 for num1, num2 in zip(y1_y2_total, y3)]
fig, ax = plt.subplots()
ax.bar(x, y_total, label='y3')
ax.bar(x, y1_y2_total, label='y2')
ax.bar(x, y1, label='y1')
ax.legend()
plt.show()
