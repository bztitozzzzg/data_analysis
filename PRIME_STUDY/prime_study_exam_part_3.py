from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import logging
import math
import pandas as pd
"""
デフォルトでは、標準出力にログを出力し、ログレベルはWARNING以上
"""
logging.basicConfig(
    format='%(levelname)s'
)

logging.debug('デバッグレベル')
logging.info('INFOレベル')
logging.warning('警告レベル')
logging.error('エラーレベル')
logging.critical('重大なエラー')
"""
実行結果
WARNING
ERROR
CRITICAL
"""

print(end='\n')

print(np.full((2, 3), np.pi))
print(np.full((2, 3), np.pi).T)
a = np.full((2, 3), np.pi).T.ravel()  # <-- .Tで転置、.ravel()で1次元化
print(a)
b = np.linspace(0, 1.25, 6)
print(b)
c = np.concatenate([a, b], axis=0)  # <-- concatenate関数で連結して、axis=0は行方向に増加
print(c)
print(a[1], c[-2])
"""
実行結果
3.141592653589793 1.0
"""

print(end='\n')

df = pd.DataFrame([[50, "a", False], [25, "b", True], [35, "c", True]])
df.index = ["01", "02", "03"]
df.columns = ["A", "B", "C"]


def judge(arg):
    if arg <= 50:
        return "low"
    elif arg < 70:
        return "middle"
    else:
        return "high"


df.iloc[:, 2] = df.loc[:, "A"] * 2
df.iloc[:, 1] = df.loc[:, "C"].apply(judge)
_ = df["C"] < 80
df = df[_]
print(df)
print(df.iloc[1, 2], df.iloc[-1, 1])

x = np.arange(0.0, 15.0, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, y1, label='sin')
ax.plot(x, y2, label='cos')
ax.legend()

plt.show()

print(end='\n')

fig, ax = plt.subplots()
x = [1, 2, 3]
y1 = [10, 2, 3]
y2 = [5, 3, 6]
labels = ['red', 'blue', 'yellow']
y_total = [num1 + num2 for num1, num2 in zip(y1, y2)]
ax.bar(x, y_total, tick_label=labels, label='y1')  # …【イ】
ax.bar(x, y2, label='y2')  # …【ウ】
ax.legend()

plt.show()

np.random.seed(123)
mu = 100
sigma = 15
x = np.random.normal(mu, sigma, 1000)
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, bins=25, orientation='horizontal')
for i, num in enumerate(n):
    print('{:.2f} - {:.2f} {}'.format(bins[i], bins[i + 1], num))

plt.show()

print(end='\n')

# スクリプトA
np.random.seed(123)
X = np.random.random(size=50)
Y = 2*X + 0.5*np.random.rand(50)
fig, ax = plt.subplots()
ax.scatter(X, Y)
plt.show()

# スクリプトB
ist = PCA(n_components=2)

X_ist = ist.fit_transform(
    np.hstack((X[:, np.newaxis], Y[:, np.newaxis])))  # …【B】

fig, ax = plt.subplots()
ax.scatter(X_ist[:, 0], X_ist[:, 1])
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
plt.show()
"""
実行結果
67.86 - 71.94 16.0
71.94 - 76.02 29.0
76.02 - 80.11 37.0
80.11 - 84.19 65.0
84.19 - 88.27 57.0
88.27 - 92.35 90.0
92.35 - 96.43 105.0
96.43 - 100.51 115.0
100.51 - 104.59 116.0
104.59 - 108.68 78.0
108.68 - 112.76 74.0
112.76 - 116.84 77.0
116.84 - 120.92 42.0
120.92 - 125.00 41.0
125.00 - 129.08 21.0
129.08 - 133.17 10.0
133.17 - 137.25 4.0
137.25 - 141.33 2.0
141.33 - 145.41 2.0
145.41 - 149.49 0.0
149.49 - 153.57 1.0
"""
