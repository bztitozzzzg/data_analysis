from matplotlib import colors
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# サポートベクタマシン
"""
分類・回帰だけでなく、外れ値検出にも使えるアルゴリズム。
直線や平面などで分離できない（線形分離できない）データを高次元の空間に
写して線形分離することにより、分類を行いアルゴリズム。
実際は、高次元の空間に写すのではなく、データ間の近さを定量化するカーネル（高次元の空間でのデータ間の内積を計算する関数に相当）
を導入する。

直線を決定境界、各クラスのデータをサポートベクタ、そしてクラス間のサポートベクタの距離を
マージンと呼ぶ。
"""
np.random.seed(123)
# X軸Y軸ともに0から1までの一様分布から100点をサンプリング
X0 = np.random.uniform(size=(100, 2))
# クラス0のラベルを100個生成
y0 = np.repeat(0, 100)
# X軸Y軸ともに-1から0までの一様分布から100点をサンプリング
X1 = np.random.uniform(-1.0, 0.0, size=(100, 2))
# クラス1のラベルを100個生成
y1 = np.repeat(1, 100)
# 散布図にプロット
fig, ax = plt.subplots()
ax.scatter(X0[:, 0], X0[:, 1], marker='o', label='label 0')
ax.scatter(X1[:, 0], X1[:, 1], marker='x', label='label 1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
plt.show()

# 学習、および決定境界、マージン、サポートベクタを可視化する関数


def plot_boundary_margin_sv(X0, y0, X1, y1, kernel, C, xmin=-1, xmax=1, ymin=-1, ymax=1):
    # サポートベクタマシンのインスタンス化
    svc = SVC(kernel=kernel, C=C)
    # 学習
    svc.fit(np.vstack((X0, X1)), np.hstack((y0, y1)))

    fig, ax = plt.subplots()
    ax.scatter(X0[:, 0], X0[:, 1], marker='o', label='class 0')
    ax.scatter(X1[:, 0], X1[:, 1], marker='x', label='class 1')

    # 決定境界とマージンをプロット
    xx, yy = np.meshgrid(np.linspace(xmin, xmax, 100),
                         np.linspace(ymin, ymax, 100))
    xy = np.vstack([xx.ravel(), yy.ravel()]).T
    p = svc.decision_function(xy).reshape((100, 100))
    ax.contour(xx, yy, p, colors='k', levels=[-1, 0, 1],
               alpha=0.5, linestyles=['--', '-', '--'])
    # サポートベクタをプロット
    ax.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1],
               s=250, facecolors='none', edgecolors='black')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(loc='best')

    plt.show()


plot_boundary_margin_sv(X0, y0, X1, y1, kernel='linear', C=1e6)
plot_boundary_margin_sv(X0, y0, X1, y1, kernel='linear', C=0.1)

np.random.seed(123)
X = np.random.random(size=(100, 2))
y = (X[:, 1] > 2*(X[:, 0]-0.5)**2 + 0.5).astype(int)
fig, ax = plt.subplots()
ax.scatter(X[y == 0, 0], X[y == 0, 1], marker='o', label='class 0')
ax.scatter(X[y == 1, 0], X[y == 1, 1], marker='x', label='class 1')
ax.legend()
plt.show()

# カーネルとして動径基底関数をもちいて２つのクラスを分離
# 決定境界、マージン、サポートベクタをプロット
X0, X1 = X[y == 0, :], X[y == 1, :]
y0, y1 = y[y == 0], y[y == 1]
plot_boundary_margin_sv(X0, y0, X1, y1, kernel='rbf', C=1e3, xmin=0, ymin=0)
