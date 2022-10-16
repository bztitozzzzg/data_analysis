import numpy as np

# ユニバーサルファンクション
# 絶対値（abs関数）
a = np.array([[-1, -2, -3, 4, 5], [6, 7, -8, -9, -10]])
print(np.abs(a))
"""
実行結果
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
"""

print(end='\n')

# ブロードキャスト
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([[10, 20, 30], [40, 50, 60]])
d = np.array([[1], [2], [3]])
# aに10を追加
print(a + 10)
"""
実行結果
[11 12 13]
"""

print(end='\n')
# a + b
print(a + b)
"""
実行結果
[5 7 9]
"""

print(end='\n')
# a + c
print(a + c)
"""
実行結果
[[11 22 33]
 [41 52 63]]
"""

print(end='\n')
# a + d
print(a + d)
"""
実行結果
[[2 3 4]
 [3 4 5]
 [4 5 6]]
"""

print(end='\n')

# inf
a = np.array([1, 2, 3])
a_inf = np.array([0, 2, 0])
print(a / a_inf)
"""
実行結果
RuntimeWarning: divide by zero encountered in divide
  print(a / a_inf)
[inf  1. inf]
"""

print(end='\n')

print(a / (a_inf + 1e-6))
"""
実行結果
[1.000000e+06 9.999995e-01 3.000000e+06]
"""

print(end='\n')

a = np.array([1, 2, 3])
b = np.array([[-1, -2, -3], [4, 5, 6]])
print(np.dot(b, a))
"""
実行結果
[-14  32]
"""

print(end='\n')

print(b @ a)
"""
実行結果
[-14  32]
"""

print(end='\n')

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[-1, -2], [3, 4], [5, 6]])
print(np.dot(a, b))
print(np.dot(b, a))
"""
実行結果
a @ b:
[[20 24]
 [41 48]]
b @ a:
[[ -9 -12 -15]
 [ 19  26  33]
 [ 29  40  51]]
"""

print(end='\n')

# 判定
a = np.array([[-1, -2], [3, 4], [5, 6]])
print(a > 0)
"""
実行結果
[[False False]
 [ True  True]
 [ True  True]]
"""

# 条件を満たす要素数（count_nonzero関数）
print(np.count_nonzero(a > 0))
"""
実行結果
4
"""
print(end='\n')
# 比較条件を満たす要素数はsum関数でも求めることができます。
print(np.sum(a > 0))
"""
実行結果
4
"""
print(end='\n')
# 存在判定（any関数）
print(np.any(a >= 5))
"""
実行結果
True
"""

# all関数
print(np.all(a > 0))
"""
実行結果
False
"""

# 条件を満たす要素の取得
print(a[a > 0])
"""
実行結果
[3 4 5 6]
"""

print(end='\n')

# 配列同士の比較
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 3, 5], [2, 4, 6]])
c = np.array([1, 2, 3])

print(a == b)
"""
実行結果
[[ True False False]
 [False False  True]]
"""

print(a == c)
"""
実行結果
[[ True  True  True]
 [False False False]]
"""

# allclose関数
print(np.allclose(a, b))
"""
実行結果
False
"""

# atolを指定（絶対誤差）
print(np.allclose(a, b, atol=10))
"""
実行結果
True
"""

print(end='\n')
print("#------------------------------------#", end='\n')
print("# 確認問題")

a = np.array([["-1", "-2", "-3", "4", "5"], [6, 7, -8, -9, -10]])
# np.abs(a)
"""
実行結果
in <module>
    np.abs(a)
numpy.core._exceptions._UFuncNoLoopError: ufunc 'absolute' did not contain a loop with signature matching types <class 'numpy.dtype[str_]'> -> None
"""

print(end='\n')

b = np.array([4, 5, 6])
print(np.log(b))
"""
実行結果
[1.38629436 1.60943791 1.79175947]
"""

print(end='\n')
a = np.array([1, 2, 3])
b = np.array([[2, 3, 4], [4, 5, 6]])

print(np.dot(b, a))
"""
実行結果
[20 32]
"""

print(end='\n')

a = np.array([1, 2, 3])
b = np.array([[2, 3, 4], [4, 5, 6]])

print(a.shape)
print(b.shape)
"""
じっこうけっか
(3,)
(2, 3)
"""

# print(np.dot(a, b))
"""
実行結果
in dot
ValueError: shapes (3,) and (2,3) not aligned: 3 (dim 0) != 2 (dim 0)
"""

print(end='\n')
a = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5,
             6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9, 10]])

print(np.any(a > 10))
"""
実行結果
False
"""
