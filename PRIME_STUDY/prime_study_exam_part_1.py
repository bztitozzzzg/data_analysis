from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

names = ['spam', 'ham', 'eggs']
lens = []
for name in names:
    lens.append(len(name))

print(lens)

"""
↓ 別解
"""
lens = [len(name) for name in names]
print(lens)

print(end='\n')

"""
Matplotlibを用いて正規分布に従うランダムな値をヒストグラムで描画する
"""
np.random.seed(123)
mu = 100
sigma = 15
x = np.random.normal(mu, sigma, 1000)
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, bins=25, orientation='horizontal')
for i, num in enumerate(n):
    print('{:.2f} - {:.2f} {}'.format(bins[i], bins[i + 1], num))

plt.show()
"""
実行結果
1回目：
51.53 - 55.62 2.0
55.62 - 59.70 3.0
59.70 - 63.78 6.0
63.78 - 67.86 7.0
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

2回目：
51.53 - 55.62 2.0
55.62 - 59.70 3.0
59.70 - 63.78 6.0
63.78 - 67.86 7.0
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

print(end='\n')

"""
決定木の深さの最適値
"""

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)
clf = DecisionTreeClassifier()
param_grid = {'max_depth': [3, 4, 5]}
cv = GridSearchCV(clf, param_grid=param_grid, cv=10)
cv.fit(X_train, y_train)
y_pred = cv.predict(X_test)
print(cv.best_params_)
print(cv.best_estimator_)
# print(y_pred)

"""
実行結果
1回目：
[1 2 2 1 0 1 1 0 0 1 2 0 1 2 2 2 0 0 1 0 0 1 0 2 0 0 0 2 2 0 2 1 0 0 1 1 2
 0 0 1 1 0 2 2 2]

2回目：
[1 2 2 1 0 1 1 0 0 1 2 0 1 2 2 2 0 0 1 0 0 1 0 2 0 0 0 2 2 0 2 1 0 0 1 1 2
 0 0 1 1 0 2 2 2]
"""
