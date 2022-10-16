import numpy as np

# 要素間の差分の取得（diff関数）
l = np.array([1, 1, 5, 2, 4])
print(np.diff(l))
"""
実行結果
[ 0  4 -3  2]
"""

print(end='\n')

# 要素同士の連結（concatenate関数）
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate([a, b]))
"""
実行結果
[1 2 3 4 5 6]
"""
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[10, 20], [30, 40]])
print(np.concatenate([c, d], axis=1))
"""
実行結果
[[ 1  2  3 10 20]
 [ 4  5  6 30 40]]
"""

e = np.array([[1, 2, 3], [4, 5, 6]])
f = np.array([[10, 20, 30], [40, 50, 60]])
print(np.vstack([e, f]))
"""
実行結果
[[ 1  2  3]
 [ 4  5  6]
 [10 20 30]
 [40 50 60]]
"""

# 2次元配列の分割（hsplit関数）
a = np.array([[1, 2, 10], [3, 4, 20], [5, 6, 30], [7, 8, 40]])

col1, col2 = np.hsplit(a, [2])
print(col1)
print(col2)
"""
実行結果
[[1 2]
 [3 4]
 [5 6]
 [7 8]]

 [[10]
 [20]
 [30]
 [40]]
"""

row1, row2 = np.vsplit(a, [2])
print(row1)
print(row2)
"""
実行結果
[[ 1  2 10]
 [ 3  4 20]]
[[ 5  6 30]
 [ 7  8 40]]
"""

print(end='\n')

# 転置
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a.T)
"""
実行結果
[[1 4 7]
 [2 5 8]
 [3 6 9]]
"""

print(end='\n')

# 次元の追加
a = np.array([1, 2, 3])

print(a[np.newaxis, :])
"""
実行結果
[[1 2 3]]
"""

print(a[:, np.newaxis])
"""
実行結果
[[1]
 [2]
 [3]]
"""

print(end='\n')

# グリッドデータ(meshgrid関数)
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7])
xx, yy = np.meshgrid(x, y)
print(xx, '\n', yy)
"""
実行結果
[[1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]]

[[5 5 5 5]
 [6 6 6 6]
 [7 7 7 7]]
"""

print(end='\n')
print("#------------------------------------#", end='\n')
print("# 確認問題")

a = np.array([[1, 2, 3], [2, 3, 4]])
print(np.diff(a))
"""
実行結果
[[1 1]
 [1 1]]
"""

print(end='\n')

a = np.array([1, 2, 3])
b = np.array([4, 5])
print(np.concatenate([a, b]))
"""
実行結果
[1 2 3 4 5]
"""

print(end='\n')

a = np.array([["a", "b", "c"], ["g", "h", "i"]])
b = np.array([["d", "e", "f"], ["j", "k", "l"]])
print(np.concatenate([a, b], axis=1))
"""
実行結果
[['a' 'b' 'c' 'd' 'e' 'f']
 ['g' 'h' 'i' 'j' 'k' 'l']]
"""

print(end='\n')

A = np.newaxis
print(np.array([1, 2, 3])[:, A])
# np.array([1, 2, 3])[:, (A)]
"""
実行結果
[[1]
　[2]
　[3]]
"""
