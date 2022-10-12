import numpy as np
# 数列を返す
print("np.arange(10):", np.arange(10))
print("np.arange(1, 11):", np.arange(1, 11))
print("np.arange(1, 11, 2):", np.arange(1, 11, 2))

print(end='\n')

# 乱数
print("np.random.random((3, 2)):", np.random.random((3, 2)))
np.random.seed(123)
print("np.random.random((3, 2)):", np.random.random((3, 2)))
print("np.random.rand(4, 2):", np.random.rand(4, 2))
print("np.random.randint(1, 10):", np.random.randint(1, 10))
print("np.random.randint(1, 10, (3, 3)):", np.random.randint(1, 10, (3, 3)))
print("np.random.uniform(0.0, 5.0, size=(2, 3)):",
      np.random.uniform(0.0, 5.0, size=(2, 3)))
# デフォルト 値 で ある 0. 0 以上、 1. 0 未満 の、 4 × 3 行列 の 2 次元 配列
print("np.random.uniform(4, 3):", np.random.uniform(4, 3))
print("np.random.randn(4, 2):", np.random.randn(4, 2))

print(end='\n')

# 同じ要素の数列を作る
print("np.zeros(3):", np.zeros(3))
print("np.zeros((2, 3)):", np.zeros((2, 3)))
print("np.ones(2):", np.ones(2))
print("np.ones((3, 4)):", np.ones((3, 4)))

print(end='\n')

# 単位行列
print("np.eye(3):", np.eye(3))

print(end='\n')

# 指定値を埋める
print("np.full(3, 3.14):", np.full(3, 3.14))
print("np.full((2,4),np.pi):", np.full((2, 4), np.pi))
print("np.array([1,2,np.nan]):", np.array([1, 2, np.nan]))

print(end='\n')

# 範囲指定で均等割りデータを作る
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))
print("np.linspace(0, np.pi, 21):", np.linspace(0, np.pi, 21))

print(end='\n')

# 要素間の差分
l = np.array([2, 2, 6, 1, 3])
print("np.diff(l):", np.diff(l))

print(end='\n')

# 連結
a = np.array([1, 2, 3])
a1 = a
print("np.concatenate([a, a1]):", np.concatenate([a, a1]))

b = np.array([[1, 2, 8], [4, 5, 8]])
b1 = np.array([[10], [20]])
print("np.concatenate([b, b1], axis=1)", np.concatenate(
    [b, b1], axis=1))  # カラム（列方向）を増やすので、axis=1と指定
print("np.hstack([b, b1])", np.hstack([b, b1]))

b2 = np.array([30, 60, 45])
print("np.vstack([b, b2]):", np.vstack([b, b2]))

print(end='\n')

# 分割
b3 = np.vstack([b, b2])
first, second = np.hsplit(b3, [2])
print("first:", first)
print("second:", second)

first1, second1 = np.vsplit(b3, [2])
print("first1:", first1)
print("second1:", second1)

print(end='\n')

# 転置
# 2次元配列の行と列を入れ替えること
print("b.T:", b.T)

print(end='\n')

# 次元追加
print("a[np.newaxis, :]:", a[np.newaxis, :])  # 行方向
print("a[:, np.newaxis]:", a[:, np.newaxis])  # 列方向

print(end='\n')

# グリッドデータの生成
m = np.arange(0, 4)
n = np.arange(4, 7)
xx, yy = np.meshgrid(m, n)
print("xx:", xx)
print("yy:", yy)

print(end='\n')
