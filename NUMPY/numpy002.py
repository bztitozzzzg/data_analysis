import numpy as np

# 1次元配列
a = np.array([1, 2, 3])

# スライス
print(a[1:])
print(a[-1])

# 2次元配列
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b[0])
print(b[1, 0])
print(b[:, 2])
print(b[1, :])
print(b[0, 1:])
print(b[:, [0, 2]])

# データ再代入
b[1, 2] = 7
print(b)
b[:, 2] = 8
print(b)

# 深いコピー
a1 = a
print("a1:", a1)
a2 = a.copy()
print("a2:", a2)
a2[0] = 6
print("a2:", a2)
print("a:", a)
