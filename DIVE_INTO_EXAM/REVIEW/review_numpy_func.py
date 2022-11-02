import numpy as np  # numpyをインポート

### 1次元配列 ###
print("### 1次元配列 ###", end="\n")
a = np.array([1, 2, 3])
print(a, end="\n")
"""
実行結果
[1 2 3]
"""

# type関数
print(type(a), end="\n")
"""
実行結果
<class 'numpy.ndarray'>
"""

# shape関数
print(a.shape, end="\n")
"""
実行結果
(3,)
↑ 1次元配列で3要素であることが確認できる
"""

### 2次元配列 ###
print("### 2次元配列 ###", end="\n")
b = np.array([[1, 2, 3], [4, 5, 6]])  # 2次元のndarrayオブジェクト

print(b, end="\n")
"""
実行結果
[[1 2 3]
 [4 5 6]]
"""

print(b.shape, end="\n")
"""
実行結果
(2, 3)
↑ 2×3行列であることが読み取れる
"""

### 変形(reshape) ###
print("### 変形(reshape) ###", end="\n")

# まずは、6要素の1次元配列を作成
c1 = np.array([0, 1, 2, 3, 4, 5])

# reshapeメソッドを使い、2×3行列の配列に変換
c2 = c1.reshape((2, 3))
print(c2, end="\n")
"""
実行結果
[[0 1 2]
 [3 4 5]]
"""

# c1.reshape((3,4))などと要素数が合わない場合は、TypeErrorが送出される
# print(c1.reshape((3, 4)))
"""
実行結果
ValueError: cannot reshape array of size 6 into shape (3,4)
"""

# ravelメソッド
# 1次元配列に戻す
c3 = c2.ravel()
print(c3, end="\n")
"""
実行結果
[0 1 2 3 4 5]
"""

# flattenメソッド
c4 = c2.flatten()  # copyを返す
print(c4, end="\n")
"""
実行結果
[0 1 2 3 4 5]
"""

### データ型(dtype) ###
print("### データ型(dtype) ###", end="\n")
# NumPy配列の要素のデータ型をdtype属性を使って確認。
print(a.dtype, end="\n")
"""
実行結果
int32
"""

### 深いコピー(copy) ###
print("### 深いコピー(copy) ###", end="\n")
a1 = a
a1[1] = 5
print(a1, end="\n")
print(a, end="\n")
"""
実行結果
[1 5 3]
[1 5 3]
"""

a2 = a.copy()
a2[0] = 6
print(a2, end="\n")
print(a, end="\n")
"""
実行結果
[6 5 3]
[1 5 3]
"""

"""
c3にravelメソッドを実行した結果を入れ
c4にflattenした結果を入れた後
c3,c4のそれぞれの要素を一部書き換え
"""
c3 = c2.ravel()
c4 = c2.flatten()
c3[0] = 6
c4[1] = 7
print(c3, end="\n")
print(c4, end="\n")
"""
実行結果
[6 1 2 3 4 5]
[0 7 2 3 4 5]
"""

"""
Python標準のリストではスライスした結果は'コピー'が渡される。
NumPyではスライスの結果は'参照'が渡される
"""
py_list1 = [0, 1]
py_list2 = py_list1[:]
py_list2[0] = 2
print(py_list1, end="\n")
print(py_list2, end="\n")
"""
実行結果
[0, 1]
[2, 1]
"""

### 数列を返す(arange) ###
print("### 数列を返す(arange) ###", end="\n")
print(np.arange(10), end="\n")
"""
実行結果
[0 1 2 3 4 5 6 7 8 9]
"""

# 引数が2つの場合
print(np.arange(1, 11), end="\n")
"""
実行結果
[ 1  2  3  4  5  6  7  8  9 10]
第一引数をスタートの値とし、第二引数の1つて前の数値までの
配列が出力される
"""

# 引数が3つの場合
print(np.arange(1, 11, 2), end="\n")
"""
実行結果
[1 3 5 7 9]
第一引数をスタートの値とし、第二引数の1つて前の数値までとし
第三引数でスタートの値から増加させる数値とした
配列が出力される
"""

### 乱数 ###
print("### 乱数 ###", end="\n")
# np.random.random関数
# 行と列のタプルを渡すと0以上、1未満の範囲の
# 乱数の2次元配列を生成
f = np.random.random((3, 2))
print(f, end="\n")
"""
実行結果
[[0.5288999  0.82369825]
 [0.97453617 0.34023318]
 [0.08359323 0.70633373]]
"""

np.random.seed(123)  # テストコードの結果を同じにするためのシード値
f = np.random.random((3, 2))
print(f, end="\n")
"""
実行結果
[[0.69646919 0.28613933]
 [0.22685145 0.55131477]
 [0.71946897 0.42310646]]
"""

# rand関数
# 0-1の範囲の乱数の配列を生成
np.random.seed(123)
f = np.random.rand(4, 2)
print(f, end="\n")
"""
実行結果
[[0.69646919 0.28613933]
 [0.22685145 0.55131477]
 [0.71946897 0.42310646]
 [0.9807642  0.68482974]]
"""

"""
# randint関数
# 第一引数以上かつ第二引数未満のランダムな値を
# 第三引数としてタプルで渡した行と列の2次元配列で生成
"""
np.random.seed(123)
f = np.random.randint(1, 10, (3, 3))
print(f, end="\n")
"""
実行結果
[[3 3 7]
 [2 4 7]
 [2 1 2]]
"""

"""
# uniform関数
# 第一引数以上かつ第二引数未満のランダムな小数値を
# 第三引数としてタプルで渡した行と列の2次元配列で生成
# 第一引数と第二引数は省略可能で
# 省略すると第一引数に0.0が、第二引数に1.0がデフォルトで指定される。
"""
np.random.seed(123)
f = np.random.uniform(0.0, 0.5, size=(2, 3))
print(f, end="\n")
"""
実行結果
[[0.34823459 0.14306967 0.11342573]
 [0.27565738 0.35973448 0.21155323]]
"""

# 第一引数と第二引数を省略した場合
f = np.random.uniform(size=(4, 3))
print(f, end="\n")
"""
実行結果
[[0.9807642  0.68482974 0.4809319 ]
 [0.39211752 0.34317802 0.72904971]
 [0.43857224 0.0596779  0.39804426]
 [0.73799541 0.18249173 0.17545176]]
"""

"""
# randn関数
# 標準正規分布からのサンプリングとしての
# 乱数の出力方法を確認
# 平均0, 分散1の分布で出力
"""
f = np.random.randn(4, 2)
print(f, end="\n")
"""
実行結果
[[ 2.20593008  2.18678609]
 [ 1.0040539   0.3861864 ]
 [ 0.73736858  1.49073203]
 [-0.93583387  1.17582904]]
"""

### 同じ要素の数列を作る ###
print("### 同じ要素の数列を作る ###", end="\n")

# zero関数
# 引数で指定した要素数の0.0が入った配列を取得
print(np.zeros(3), end="\n")
"""
実行結果
[0. 0. 0.]
"""

# 2要素のタプルを渡し、指定した行列数の2次元配列を作成
print(np.zeros((2, 3)), end="\n")
"""
実行結果
[[0. 0. 0.]
 [0. 0. 0.]]
"""

# ones関数
# 引数で指定した要素数が1.0が入った配列を取得
print(np.ones(2), end="\n")
"""
実行結果
[1. 1.]
"""

# 2次元配列を作る場合は、np.zerosと同様にタプルを渡すことができる
print(np.ones((3, 4)), end="\n")
"""
実行結果
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
"""

### 単位行列 ###
print("### 単位行列 ###", end="\n")

# eye関数
# 指定する対角要素を持った単位行列を作成
print(np.eye(3), end="\n")
"""
実行結果
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""

### 指定値で埋める ###
print("### 指定値で埋める ###", end="\n")
# full関数
print(np.full(3, 3.14), end="\n")
"""
実行結果
[3.14 3.14 3.14]
"""

# 行と列を指定
# NumPyの定数値で円周率πを表す
# np.piを用いる
print(np.full((2, 4), np.pi), end="\n")
"""
実行結果
[[3.14159265 3.14159265 3.14159265 3.14159265]
 [3.14159265 3.14159265 3.14159265 3.14159265]]
"""

### 範囲指定で均等割りデータを作る ###
print("### 範囲指定で均等割りデータを作る ###", end="\n")

# linspace関数
# 0から1までを等間隔に区切った5つの要素の配列を作成
print(np.linspace(0, 1, 5), end="\n")
"""
実行結果
[0.   0.25 0.5  0.75 1.  ]
"""

### 要素間の差分 ###
print("### 要素間の差分 ###", end="\n")

# np.diff関数
# 要素間の差分を返す
l = np.array([2, 2, 6, 1, 3])
print(np.diff(l), end="\n")
"""
実行結果
[ 0  4 -5  2]
"""

### 連結 ###
print("### 連結 ###", end="\n")

# concatenate関数
# 連結を行う
print(np.concatenate([a, a1]), end="\n")
"""
実行結果
[1 5 3 1 5 3]
"""

# カラム方向（列方向）に増やすので、axis=1と指定
b1 = np.array([[10], [20]])
print(b, end="\n")
print(b1, end="\n")
print(np.concatenate([b, b1], axis=1), end="\n")
"""
実行結果
[[ 1  2  3 10]
 [ 4  5  6 20]]
"""

# hstack関数
# concatenate([x,y], axis=1)と同様
print(np.hstack([b, b1]), end="\n")
"""
実行結果
[[ 1  2  3 10]
 [ 4  5  6 20]]
"""

# vstack関数
# 行を増やす方向に連結
b2 = np.array([30, 60, 45])
b3 = np.vstack([b, b2])
print(b3, end="\n")
"""
実行結果
[[ 1  2  3]
 [ 4  5  6]
 [30 60 45]]
"""

### 分割 ###
print("### 分割 ###", end="\n")

# hsplit関数
# 列の途中で分割し2つの2次元配列を作る
# 第二引数に[2]と指定しています。
# 1つ目の配列が2列となり、残りが1列がもう一つの列になる
first, second = np.hsplit(b3, [2])
print(first, end="\n")
print(second, end="\n")
"""
実行結果
[[ 1  2]
 [ 4  5]
 [30 60]]

[[ 3]
 [ 6]
 [45]]
"""

# vsplit関数
# 行方向に分割する
first1, second1 = np.vsplit(b3, [2])
print(first1, end="\n")
print(second1, end="\n")
"""
実行結果
[[1 2 3]
 [4 5 6]]

[[30 60 45]]
"""

### 転置 ###
print("### 転置 ###", end="\n")

# 2次元配列の行と列を入れ替える
print(b, end="\n")
print(b.T, end="\n")
"""
実行結果
[[1 2 3]
 [4 5 6]]

[[1 4]
 [2 5]
 [3 6]]
"""

### 次元追加 ###
print("### 次元追加 ###", end="\n")

# 行方向を指定するスライシングにnp.newaxisを指定し次元を1つ増やす
print(a, end="\n")
print(a[np.newaxis, :], end="\n")
"""
実行結果
[1 5 3]

[[1 5 3]]
"""

# 列方向を指定するスライシングにnp.newaxisを指定する
print(a[:, np.newaxis], end="\n")
"""
実行結果
[[1]
 [5]
 [3]]
"""

### グリッドデータの作成 ###
print("### グリッドデータの作成 ###", end="\n")

# meshgrid関数
# 2次元上の点に対応する等高線やヒートマップなどを描く
# x座標、y座標の配列から、それらを組み合わせてできる
# すべての点の座標データを生成
m = np.arange(0, 4)
n = np.arange(4, 7)
xx, yy = np.meshgrid(m, n)
# mとnを行方向と列方向に方眼上（グリッド）のデータを生成
print(xx, end="\n")
print(yy, end="\n")
"""
実行結果
[[0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]]

[[4 4 4 4]
 [5 5 5 5]
 [6 6 6 6]]
"""
"""
NumPyの各機能
"""
from turtle import end_fill
import numpy as np

a = np.arange(3)
b = np.arange(-3, 3).reshape((2, 3))
c = np.arange(1, 7).reshape((2, 3))
d = np.arange(6).reshape((3, 2))
e = np.linspace(-1, 1, 10)
print(a, end="\n\n")
print(b, end="\n\n")
print(c, end="\n\n")
print(d, end="\n\n")
print(e, end="\n\n")
"""
実行結果
[0 1 2]

[[-3 -2 -1]
 [ 0  1  2]]

[[1 2 3]
 [4 5 6]]

[[0 1]
 [2 3]
 [4 5]]

[-1.         -0.77777778 -0.55555556 -0.33333333 -0.11111111  0.11111111
  0.33333333  0.55555556  0.77777778  1.        ]
"""
print(a.shape, end="\n\n")
print(b.shape, end="\n\n")
print(c.shape, end="\n\n")
print(d.shape, end="\n\n")
print(e.shape, end="\n\n")
"""
実行結果
(3,)

(2, 3)

(2, 3)

(3, 2)

(10,)
"""

### ユニバーサルファンクション ###
print("### ユニバーサルファンクション ###", end="\n")

li = [[-3, -2, -1], [0, 1, 2]]
new = []
for i, j in enumerate(li):
    new.append([])
    for k in j:
        new[i].append(abs(k))
print(new, end="\n")
"""
実行結果
[[3, 2, 1], [0, 1, 2]]
"""

# np.abs関数
# 内部要素の計算結果を取得
print(np.abs(b), end="\n")
"""
実行結果
[[3 2 1]
 [0 1 2]]
"""

# sin関数
print(np.sin(e), end="\n")
"""
実行結果
[-0.84147098 -0.70169788 -0.52741539 -0.3271947  -0.11088263  0.11088263
  0.3271947   0.52741539  0.70169788  0.84147098]
"""

# cos関数
print(np.cos(e), end="\n")
"""
実行結果
[0.54030231 0.71247462 0.84960756 0.94495695 0.99383351 0.99383351
 0.94495695 0.84960756 0.71247462 0.54030231]
"""

# log関数
# ネイピア数を底とする自然対数logをlog関数にて計算する
print(np.log(a), end="\n")
"""
実行結果
[      -inf 0.         0.69314718]
"""

# -inf　は、マイナス無限大を意味する
# log(x)は、x>0の時のみ定義されているため
# 常用対数（logの底が'10'の時）は、log10関数で計算可能
print(np.log10(c), end="\n")
"""
実行結果
[[0.         0.30103    0.47712125]
 [0.60205999 0.69897    0.77815125]]
"""

# 自然対数の底eについて
# e^xを表すために、exp関数がある
print(np.exp(a), end="\n")
"""
実行結果
[1.         2.71828183 7.3890561 ]
"""

### ブロードキャスト ###
print("### ブロードキャスト ###", end="\n")
a1 = a[:, np.newaxis]
print(a, end="\n")
print(a1, end="\n")
print(a + a1)
"""
実行結果
[[0 1 2]
 [1 2 3]
 [2 3 4]]

1次元の配列aが、3行に拡張され、3×1行列の2次元配列が
3×3行列に拡張されて足し算される

aの拡張後
[[0 1 2]
 [0 1 2]
 [0 1 2]]

a1の拡張後
[[0 0 0]
 [1 1 1]
 [2 2 2]]
"""

### 判定・論理値 ###
print("### 判定・論理値 ###", end="\n")

# 配列とスカラーを演算子で比較すると、比較結果の真偽値（True/False）が同じ形状の配列で出力される

print(a > 1, end="\n")
"""
実行結果
[False False  True]
"""

print(b > 0, end="\n")
"""
実行結果
[[False False False]
 [False  True  True]]
"""

# count_nonzeroメソッド
# 0でない要素数を出力
# PythonではFalseを0として扱う
print(np.count_nonzero(b > 0), end="\n")
"""
実行結果
2
"""

# sumメソッド
# 要素の値をすべて足す
print(np.sum(b > 0), end="\n")
"""
実行結果
2
"""

# anyメソッド
# 要素の中にTrueが含まれているかどうかを判定
print(np.any(b > 0), end="\n")
"""
実行結果
True
"""

# allメソッド
# 要素のすべてがTrueかどうか判定
print(np.all(b > 0), end="\n")
"""
実行結果
False
"""

"""
条件に合致したものだけの要素を
新たな配列として出力
"""
print(b[b > 0], end="\n")
"""
実行結果
[1 2]
"""

# allcloseメソッド
# 配列同士が同じ要素で構成されているかを確認
print(np.allclose(b, c), end="\n")
"""
実行結果
False
"""

### 関数とメソッド ###
print("### 関数とメソッド ###", end="\n")

# np.sum関数
# 要素の合計を求める
print(np.sum(a), end="\n")
print(a.sum(), end="\n")
"""
実行結果
3
"""

print(end="\n\n")
print("*** DIVE INTO EXAM 問12 ***", end="\n")
a = np.array([[0, 1, 10], [0, 1, 10]])
print(a.reshape(3, 2), end="\n\n")
print(a, end="\n\n")
b = np.array([[100], [100]])
print(b, end="\n\n")
c = np.concatenate([a, b], axis=1)
print(c, end="\n\n")
c = c.reshape(4, 2)
print(c, end="\n\n")
print(np.dot(c, b), end="\n\n")

print("*** DIVE INTO EXAM 問19 ***", end="\n")
A = np.array([[1, 3, 5]])
print(A, end="\n\n")
B = np.array([[6, 8, 10]])
print(B, end="\n\n")
C = np.concatenate([A, B], axis=0)
print(C, end="\n\n")
D = np.diff(C, axis=1)
print(D, end="\n\n")
print(np.sum(D))
