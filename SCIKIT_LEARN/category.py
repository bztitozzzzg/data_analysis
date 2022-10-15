# 分類モデル構築の流れ
"""
学習データセット、テストデータセット
学習データセットを用いて分類モデルを構築し（学習と呼ばれる）
構築したモデルのテストデータセットに対する予測を行い、未知のデータに対する
対応能力（汎化能力）を評価する。

学習データセットとテストデータセットの分割を繰り返し、モデルの構築と評価を
複数回行う方法を交差検証と呼ぶ。
"""

from cProfile import label
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# irisデータセットを読み込む
iris = load_iris()
X, y = iris.data, iris.target

# 先頭5行を表示
print('X:')
print(X[:5, :])
print('y:')
print(y[:5])

"""
Irisデータセットは、150枚のアヤメの「がく」や「花びら」の長さと幅、そして
花の種類を記録している
このデータを学習データとテストデータに分けるためにmodel_selectionモジュールの
train_test_split関数を使用する。
train_test_split関数の1番目の引数には説明変数（特徴量）を表す
NumPy配列やpandasのDataFrame、2番目の引数には目的変数を表す
NumPy配列を指定する。
引数test_sizeにはテストデータの割合を、引数random_stateには
データを分割する際に用いるシード値を固定するための値を整数で指定する。
"""

# 学習データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
