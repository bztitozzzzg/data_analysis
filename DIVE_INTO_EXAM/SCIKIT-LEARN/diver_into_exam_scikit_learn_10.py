from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
data, target = iris.data[:100, :], iris.target[:100]
data_train, data_test, target_train, target_test = train_test_split(
    data, target, random_state=123, test_size=0.2)

tree = DecisionTreeClassifier(max_depth=3)
tree.fit(data_train, target_train)
target_pred = tree.predict(data_test)

print(end='\n')
print('******分類精度の評価******')

print(classification_report(target_test, target_pred), end='\n')
"""
実行結果
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         9
           1       1.00      1.00      1.00        11

    accuracy                           1.00        20
   macro avg       1.00      1.00      1.00        20
weighted avg       1.00      1.00      1.00        20
"""

print('******交差検証******')
cross_val_score(tree, data, target, cv=10, scoring='accuracy')
print(cross_val_score(tree, data, target, cv=10, scoring='accuracy'))
"""
実行結果
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
"""
