from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
data, target = iris.data, iris.target
data_train, data_test, target_train, target_test = train_test_split(
    data, target, random_state=123, test_size=0.2)
forest = RandomForestClassifier(n_estimators=100, random_state=123)
forest.fit(data_train, target_train)
print(forest.fit(data_train, target_train))

print(end='\n')

y_pred = forest.predict(data_test)
y_pred
print(y_pred)
"""
実行結果
[1 2 2 1 0 1 1 0 0 1 2 0 1 2 2 2 0 0 1 0 0 1 0 2 0 0 0 2 2 0]
"""
