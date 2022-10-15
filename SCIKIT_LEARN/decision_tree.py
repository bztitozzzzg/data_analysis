# 決定木
"""
treeモジュールのDecisionTreeClassifierクラスを使用する。
DecisionTreeClassifierクラスのインスタンスを生成し
fitメソッドで学習、predictメソッドでテストデータセットに対する予測を実行。
DecisionTreeClassifierクラスをインスタンス化する時の変数max_depth=3とすることで
木の最大の深さを3に指定する。
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from pydotplus import graph_from_dot_data

# Irisデータセットを読み込む
iris = load_iris()
X, y = iris.data, iris.target

# 学習データセットとテストデータに分割する
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)

# 決定木をインスタンス化する（木の最大の深さ＝3）
tree = DecisionTreeClassifier(max_depth=3)

# 学習
tree.fit(X_train, y_train)

# dot形式のデータを抽出
dot_data = export_graphviz(tree, filled=True, rounded=True, class_names=[
                           'Setosa', 'Versicolor', 'Virginica'], feature_names=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'], out_file=None)

# 決定木のプロットを出力
graph = graph_from_dot_data(dot_data)
graph.progs = {'dot': u"C:\\Program Files\\Graphviz\\bin\\dot.exe"}
graph.write_png('tree.png')
