import numpy as np

# 1次元配列
a = np.array([1, 2, 3])

print(a)
print(type(a))
print(a.shape)

# 2次元配列
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)
print(b.shape)

# 変形
c1 = np.array([0, 1, 2, 3, 4, 5])

print(c1)

"""
reshapeメソッドは、要素数が重要
c1.reshape((3, 4))などと要素数が合っていない場合
エラー(ValueError)になる
"""
c2 = c1.reshape((2, 3))  # 2 × 3行列の配列に変換
print(c2)

"""
ravelメソッドとflattenメソッドの違い
ravelは参照を返却
flattenはコピーを返却
"""
c3 = c2.ravel()  # 1次元配列に戻す
print(c3)

c4 = c2.flatten()  # copyを返す
print(c4)

# データ型(dtype)
print(a.dtype)

d = np.array([1, 2], dtype=np.int16)
print(d)
print(d.astype(np.float16))
