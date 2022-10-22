import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
data = iris.data[:, [1, 3]]
fig, ax = plt.subplots()
ax.scatter(data[:, 0], data[:, 1])
ax.set_xlabel('sepal width (cm)')
ax.set_ylabel('petal width (cm)')
plt.show()

km = KMeans(n_clusters=3, init='random', n_init=10, random_state=123)
data_km = km.fit_predict(data)
print(data_km)
"""
実行結果
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 2 0 0 0 0 0 0 0 0 2 2 2 2 2 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 2 2
 2 2 2 1 2 2 2 2 2 2 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 2 1 2 1 1
 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 2 1 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1]
"""

print(end='\n')
data[data_km == 0, 0]
print(data[data_km == 0, 0])
"""
実行結果
[3.5 3.  3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 3.7 3.4 3.  3.  4.  4.4 3.9 3.5
 3.8 3.8 3.4 3.7 3.6 3.3 3.4 3.  3.4 3.5 3.4 3.2 3.1 3.4 4.1 4.2 3.1 3.2
 3.5 3.6 3.  3.4 3.5 3.2 3.5 3.8 3.  3.8 3.2 3.7 3.3]
"""

print(end='\n')
data[data_km == 0, 1]
print(data[data_km == 0, 1])
"""
実行結果
[0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 0.2 0.2 0.1 0.1 0.2 0.4 0.4 0.3
 0.3 0.3 0.2 0.4 0.2 0.5 0.2 0.2 0.4 0.2 0.2 0.2 0.2 0.4 0.1 0.2 0.2 0.2
 0.2 0.1 0.2 0.2 0.3 0.2 0.6 0.4 0.3 0.2 0.2 0.2 0.2]
"""

fig, ax = plt.subplots()
# group 1
ax.scatter(data[data_km == 0, 0], data[data_km == 0, 1],
           s=30, marker='o', label='group 1')
# group 2
ax.scatter(data[data_km == 1, 0], data[data_km == 1, 1],
           s=30, marker='v', label='group 2')
# group 3
ax.scatter(data[data_km == 2, 0], data[data_km == 2, 1],
           s=30, marker='s', label='group 3')

ax.set_xlabel('sepal width (cm)')
ax.set_ylabel('petal width (cm)')
ax.legend(loc='best')
plt.show()
