from IPython.display import Image
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
data, target = iris.data, iris.target
data_train, data_test, target_train, target_test = train_test_split(
    data, target, random_state=123, test_size=0.2)
"""
実行結果

"""

print(end='\n')
print('******学習******')
tree = DecisionTreeClassifier(max_depth=3)
tree.fit(data_train, target_train)
print(tree.fit(data_train, target_train))

print(end='\n')
dot_data = export_graphviz(tree, filled=True, rounded=True, class_names=['Setosa', 'Versicolor', 'Virginica'], feature_names=[
                           'Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'], out_file=None)
graph = graph_from_dot_data(dot_data)
graph.write_png('tree.png')
print(graph.write_png('tree.png'))
"""
実行結果
True
"""

print(end='\n')

Image('tree.png')

print(end='\n')
target_pred = tree.predict(data_test)
target_pred
print(target_pred)
"""
実行結果
[1 2 2 1 0 1 1 0 0 1 2 0 1 2 2 2 0 0 1 0 0 1 0 2 0 0 0 2 2 0]
"""
