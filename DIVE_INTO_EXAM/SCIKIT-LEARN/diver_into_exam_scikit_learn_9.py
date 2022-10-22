from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
data, target = iris.data, iris.target
data_train, data_test, target_train, target_test = train_test_split(
    data, target, random_state=123, test_size=0.2)

print(end='\n')
print('******交差検証******')
tree = DecisionTreeClassifier()
tree_depth = {'max_depth': [2, 3, 4, 5]}
clf = GridSearchCV(tree, param_grid=tree_depth, cv=10)
clf.fit(data_train, target_train)
print(clf)
"""
実行結果
GridSearchCV(cv=10, estimator=DecisionTreeClassifier(),
             param_grid={'max_depth': [2, 3, 4, 5]})
"""

print(end='\n')
print('******最適値******')
clf.best_params_
print(clf.best_params_, end='\n')
"""
実行結果
{'max_depth': 4}
"""
clf.best_estimator_
print(clf.best_estimator_, end='\n')
"""
実行結果
DecisionTreeClassifier(max_depth=4)
"""

target_pred = clf.predict(data_test)
target_pred
print(target_pred, end='\n')
"""
実行結果
[1 2 2 1 0 1 1 0 0 1 2 0 1 2 2 2 0 0 1 0 0 1 0 2 0 0 0 2 2 0]
"""
