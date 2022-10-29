from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame([[40, "a", True], [20, "b", False], [30, "c", False]])
df.index = ["01", "02", "03"]
df.columns = ["A", "B", "C"]

print(df)


def judge(arg):
    if arg < 50:
        return "low"
    elif arg < 70:
        return "middle"
    else:
        return "high"


# v-- 全行の1列目（40, 20, 30）を2倍にした要素を、全行の3列目に挿入。
df.loc[:, "C"] = df.iloc[:, 0] * 2
print(df)
df.loc[:, "B"] = df.iloc[:, 2].apply(judge)
print(df)
_ = df["C"] > 50
print(_)
df = df[_]

print(df.iloc[0, 2], df.loc["03", "B"])

print(end='\n')

fig, ax = plt.subplots()
x = [1, 2, 3]
y1 = [10, 2, 3]
y2 = [5, 3, 6]
labels = ['Setosa', 'Versicolor', 'Virginica']
# y_total = [num1 + num2 for num1, num2 in sum(y1, y2)] <-- sum関数は、intなのでNG
y_total = [num1 + num2 for num1, num2 in zip(y1, y2)]
ax.bar(x, y_total, tick_label=labels, label='y1')
ax.bar(x, y2, label='y2')
ax.legend()
plt.show()

print(end='\n')

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

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)
clf = DecisionTreeClassifier()
param_grid = {'max_depth': [3, 4, 5]}
cv = GridSearchCV(clf, param_grid=param_grid, cv=10)
cv.fit(X_train, y_train)
y_pred = cv.predict(X_test)
print(y_pred)

a = np.full((2, 3), np.pi).T.ravel()
b = np.linspace(0, 1, 5)
print(b)
c = np.hstack([a, b])
print(a[-1], c[-2])
