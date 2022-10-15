# ランダムフォレスト
"""
データのサンプルと特徴量（説明変数）をランダムに選択して決定木を構築する処理を
複数回繰り返し、各木の推定結果の多数決や平均値による分類・回帰を行う手法。
ランダムに選択されたサンプルと特徴量（説明変数）のデータを"ブートストラップデータ"と呼ぶ。
ランダムフォレストは決定木のアンサンブル（集合）であり、このように複数の学習器を用いた
学習方法は"アンサンブル学習"と呼ぶ。
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Irisデータセットを読み込む
iris = load_iris()
X, y = iris.data, iris.target

# 学習データセットとテストデータに分割する
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)

# ランダムフォレストをインスタンス化する
forest = RandomForestClassifier(n_estimators=100, random_state=123)
# 学習
forest.fit(X_train, y_train)
# 予測
y_pred = forest.predict(X_test)
print(y_pred)
