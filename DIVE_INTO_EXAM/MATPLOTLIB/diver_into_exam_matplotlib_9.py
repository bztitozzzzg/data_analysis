import pandas as pd
import matplotlib.pyplot as plt

# data1
x1 = [1, 2, 3, 4]
y1 = [5, 4, 7, 8]
# data2
x2 = [1, 2, 3, 4]
y2 = [4, 3, 6, 7]

fig, ax = plt.subplots()
ax.plot(x1, y1, label='data1')
ax.bar(x2, y2, label='data2')
ax.legend()
plt.show()

print(end='\n')

df = pd.DataFrame({'data1': [3, 2, 1], 'data2': [1, 4, 2]})
# df.plot()
# df.plot.bar()
df.plot.bar(stacked=True)
plt.show()

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
# fig.savefig('sample_bar_graph.png')

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y, color='red')
plt.show()

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.bar(x, y, color='white', edgecolor='red')
plt.show()

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=10)
plt.show()

print(end='\n')

x = [1, 2, 3]
y = [2, 4, 6]

fig, ax = plt.subplots()
ax.plot(x, y, linestyle='--')
plt.show()

print(end='\n')

x1 = [1, 2, 3]
y1 = [2, 4, 6]
x2 = [1, 2, 3]
y2 = [6, 4, 2]

fig, ax = plt.subplots()
ax.plot(x1, y1, linestyle='-.')
ax.plot(x2, y2, linestyle=':')
plt.show()

print(end='\n')

fig, ax = plt.subplots()
ax.set_title('Edit font style')
plt.show()

print(end='\n')

fig, ax = plt.subplots()
ax.set_title('Edit font style', family='monospace', size=20, weight='bold')
plt.show()

print(end='\n')

fontdict = {
    'family': 'monospace',
    'size': 20,
    'weight': 'bold'
}

fig, ax = plt.subplots()
ax.set_title('Graph title', fontdict=fontdict, size=30)
ax.set_xlabel('x label', fontdict=fontdict)
ax.set_ylabel('y label', fontdict=fontdict)
plt.show()

print(end='\n')

fig, ax = plt.subplots()
ax.text(0.2, 0.5, 'DIVE INTO CODE', size=20)
plt.show()
