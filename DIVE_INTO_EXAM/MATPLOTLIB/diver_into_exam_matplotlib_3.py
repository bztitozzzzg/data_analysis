import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [8, 2, 4]

fig, ax = plt.subplots()
ax.bar(x, y)
plt.show()
"""
実行結果
"""

print(end='\n')

x = [1, 2, 3]
y = [8, 2, 4]

fig, ax = plt.subplots()
labels = ['label 1', 'label 2', 'label 3']
# 省略
# ax.bar(x, y, tick_label=labels)
ax.barh(x, y, tick_label=labels)
# 省略
plt.show()

print(end='\n')

fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [4, 12, 5]
y2 = [8, 2, 4]

ax.bar(x, y1, label='y1')
ax.bar(x, y2, label='y2')
ax.legend()
plt.show()

print(end='\n')

fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [4, 12, 5]
y2 = [8, 2, 4]
width = 0.4
ax.bar(x, y1, width=width, label='y1')
ax.bar(x, y2, width=width, label='y2')
ax.legend()
plt.show()

print(end='\n')

fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [4, 12, 5]
y2 = [8, 2, 4]
width = 0.4
# y1
ax.bar(x, y1, width=width, label='y1')
# y2
x2 = [num + width for num in x]
ax.bar(x2, y2, width=width, label='y2')
ax.legend()
plt.show()

print(end='\n')

fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [4, 12, 5]
y2 = [8, 2, 4]
labels = ['Apple', 'Banana', 'Orange']
width = 0.4

ax.bar(x, y1, width=width, label='y1')
x2 = [num + width for num in x]
ax.bar(x2, y2, width=width, label='y2')
ax.legend()
plt.xticks(x, labels)
plt.show()

print(end='\n')

fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [4, 12, 5]
y2 = [8, 2, 4]
labels = ['Apple', 'Banana', 'Orange']
width = 0.4

ax.bar(x, y1, width=width, label='y1')

x2 = [num + width for num in x]
ax.bar(x2, y2, width=width, label='y2')
ax.legend()

label_axis = [num + width/2 for num in x]
plt.xticks(label_axis, labels)
plt.show()
