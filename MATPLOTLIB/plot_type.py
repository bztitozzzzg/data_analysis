import matplotlib.pyplot as plt
import numpy as np

# 折れ線グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [1, 2, 3]
y2 = [3, 1, 2]
ax.plot(x, y1)  # 折れ線グラフを描画
ax.plot(x, y2)

plt.show()

# sin,cosカーブ曲線
x = np.arange(0.0, 15.0, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1, label='sin')
ax.plot(x, y2, label='cos')
ax.legend()

plt.show()

# 棒グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y = [10, 2, 3]
ax.bar(x, y)  # 棒グラフを描画

plt.show()

# tick_label引数で目盛り設定
fig, ax = plt.subplots()
x = [1, 2, 3]
y = [10, 2, 3]
labels = ['spam', 'ham', 'egg']
# ax.bar(x, y, tick_label=labels)  # ラベルを指定
ax.barh(x, y, tick_label=labels)  # ラベルを指定

plt.show()

# 複数の棒グラフを描画
fig, ax = plt.subplots()
x = [1, 2, 3]
y1 = [10, 2, 3]
y2 = [5, 3, 6]
labels = ['spam', 'ham', 'egg']

# y1とy2を足した値を格納
y_total = [num1 + num2 for num1, num2 in zip(y1, y2)]

# y1とy2を足した高さの棒グラフを描画
ax.bar(x, y_total, tick_label=labels, label='y1')
ax.bar(x, y2, label='y2')
ax.legend()

plt.show()
