import numpy as np

# sum関数
a = np.array([1, 2, 3])
print(np.sum(a))
print(a.sum())  # 別の記載方法
"""
実行結果
6
"""

print(end='\n')

# データ型確認（dtypeメソッド）
print(a.dtype)
"""
実行結果
int32
"""

print(end='\n')

# データ型の指定
a = np.array([1, 2, 3], dtype=np.int16)
print(a.dtype)
"""
実行結果
int16
"""

print(end='\n')

# データ型の変換（astypeメソッド）
print(a.astype(np.float16))
"""
実行結果
[1. 2. 3.]
"""

print(end='\n')

# 次元変換
# 1次元配列を作成
c1 = np.array([1, 2, 3, 4, 5, 6])
# reshapeメソッドを使って2行3列の2次元配列に変換
c2 = c1.reshape((2, 3))
print(c2)
"""
実行結果
[[1 2 3]
 [4 5 6]]
"""
# 要素数が足りない場合、割り切れない場合はエラー（ValueError）となる。
# c3 = c1.reshape((2, 4))
"""
実行結果
ValueError: cannot reshape array of size 6 into shape (2,4)
"""

print(end='\n')

# ravelメソッド
c4 = c2.ravel()
print(c4)
"""
実行結果
[1 2 3 4 5 6]
"""

print(end='\n')

# flattenメソッド
c5 = c2.flatten()
print(c5)
"""
実行結果
[1 2 3 4 5 6]
"""

print(end='\n')

# 複製（copyメソッド）
a = np.array([1, 2, 3])
a1 = a
a1[2] = 5
print(a1)
print(a)
"""
実行結果
a1:[1 2 5]
a:[1 2 5]
"""
a = np.array([1, 2, 3])
a2 = a.copy()
a2[2] = 10
print(a2)
print(a)
"""
実行結果
a2:[1 2 10]
a:[1 2 3]
"""
print(end='\n')
# 数列（arangeメソッド）
print(np.arange(10))
"""
実行結果
[0 1 2 3 4 5 6 7 8 9]
"""

print(np.arange(1, 11))
"""
実行結果
[ 1  2  3  4  5  6  7  8  9 10]
"""

# 特定の間隔を開けた数列を定義したい場合は、引数を3つ渡す。
# 試しに、3つ目の引数に2を渡し、2ずつ間隔を開けた数列からなる配列
print(np.arange(1, 11, 2))
"""
実行結果
[1 3 5 7 9]
"""
print(end='\n')

# 乱数（random関数）
# randomモジュールからrandom関数を呼び出す必要がある。
# 4行2列からなる2次元行列をrandom関数を使って定義する
f_array = np.random.random((4, 2))
print(f_array)
"""
実行結果
[[0.43928873 0.48399799]
 [0.19953116 0.74998347]
 [0.27821324 0.96137261]
 [0.44902394 0.84121299]]
"""
print(end='\n')
# seed関数
np.random.seed(123)
f_array = np.random.random((4, 2))
print(f_array)
"""
実行結果
[[0.69646919 0.28613933]
 [0.22685145 0.55131477]
 [0.71946897 0.42310646]
 [0.9807642  0.68482974]]
"""
print(end='\n')
# randint関数
np.random.seed(123)
i_array = np.random.randint(1, 10)
print(i_array)
"""
実行結果
3
"""

print(end='\n')

# 3行5列からなる2次元配列を定義
np.random.seed(123)
i_array = np.random.randint(1, 10, (3, 5))
print(i_array)
"""
実行結果
[[3 3 7 2 4]
 [7 2 1 2 1]
 [1 4 5 1 1]]
"""

print(end='\n')

# uniform関数
# ランダムな少数値を使った2次元配列を定義したい場合、randomモジュールのuniform関数を使用する。
# 試しに、0.0以上5.0未満の4行2列からなる2次元配列を定義する。
np.random.seed(123)
print(np.random.uniform(0.0, 5.0, size=(4, 2)))
"""
実行結果
[[3.48234593 1.43069667]
 [1.13425727 2.75657385]
 [3.59734485 2.1155323 ]
 [4.90382099 3.42414869]]
"""

print(end='\n')

np.random.seed(123)
print(np.random.uniform(size=(4, 2)))
"""
実行結果
[[0.69646919 0.28613933]
 [0.22685145 0.55131477]
 [0.71946897 0.42310646]
 [0.9807642  0.68482974]]
"""

print(end='\n')

# randn関数
# 上記の乱数はすべて一様乱数と呼ばれ、特定の範囲からランダムに値を取得するもの。
# 一方、randn関数は平均0、分散1の標準正規分布からランダムに値を取り出す。
# 試しに、標準正規分布の値からなる4行3列の2次元配列を定義する。
np.random.seed(123)
print(np.random.randn(4, 3))
"""
実行結果
[[-1.0856306   0.99734545  0.2829785 ]
 [-1.50629471 -0.57860025  1.65143654]
 [-2.42667924 -0.42891263  1.26593626]
 [-0.8667404  -0.67888615 -0.09470897]]
"""

print(end='\n')

# zeros・ones関数
print(np.zeros(3))
"""
実行結果
[0. 0. 0.]
"""

# zeros関数は引数にタプルを渡すことで、2次元配列を定義する。
print(np.zeros((3, 4)))
"""
実行結果
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""

print(end='\n')

# ones関数
# zeros関数と同じようにones関数を使用することで、1.0が連続する配列も定義できる。
print(np.ones((2, 3)))
"""
実行結果
[[1. 1. 1.]
 [1. 1. 1.]]
"""

print(end='\n')

# eye関数
print(np.eye(4))
"""
実行結果
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
"""

print(end='\n')

# full関数
print(np.full(5, 10))
"""
実行結果
[10 10 10 10 10]
"""

print(np.full((2, 3), np.pi))
"""
実行結果
[[3.14159265 3.14159265 3.14159265]
 [3.14159265 3.14159265 3.14159265]]
"""

print(end='\n')

# nan
print(np.array([1, 2, 3, np.nan]))
"""
実行結果
[ 1.  2.  3. nan]
"""

print(end='\n')

# linspace関数
print(np.linspace(0, 1, 5))
"""
実行結果
[0.   0.25 0.5  0.75 1.  ]
"""
print("#------------------------------------#", end='\n')
print("# 確認問題")

print(np.sum([[1, 2], [2, 3], [4, 5]], 0))
"""
実行結果
[ 7 10]
"""

print(end='\n')

print(np.array([0.0, 0.1]).dtype)
"""
実行結果
float64
"""

print(end='\n')

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a.reshape(5, 2))
"""
実行結果
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]]
"""

print(end='\n')

print(np.arange(2, 5, 2))
"""
実行結果
[2 4]
"""

print(end='\n')

a = np.array([[1, 2, 3], [2, 3, 4]])
b = a
a[0][0] = 0
b[0][0] = 1
print(a[0][0])
"""
実行結果
1
"""
