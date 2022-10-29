"""
決定木コード
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from yaml import load

# Irisデータセットをロード
iris = load_iris()
X, y = iris.data, iris.target

# 学習データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)

# 決定木をインスタンス化
clf = DecisionTreeClassifier()
param_grid = {'max_depth': [3, 4, 5]}

# 10分割の交差検証を実行
cv = GridSearchCV(clf, param_grid=param_grid, cv=10)
cv.fit(X_train, y_train)

# 最適な深さを確認する
print(cv.best_params_)
