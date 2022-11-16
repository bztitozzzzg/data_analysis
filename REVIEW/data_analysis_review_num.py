import numpy as np

# 1次元配列
a = np.array([1, 2, 3])
print(a)
print(type(a))
print(a.shape) # <<< (3,) は1次元配列の3要素　という意味

# 2次元配列
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(type(b))
print(b.shape) # <<< (2,3)は2×3行列 という意味

"""
変形（reshape）
"""
c1 = np.array([0, 1, 2, 3, 4, 5])
print(c1)
c2 = c1.reshape(2,3)
print(c2) # <<< 2×3行列に変換
c3 = c2.ravel()
print(c3) # <<< 2次元配列を1次元配列に戻す

c4 = c2.flatten()
print(c4) # <<< copyを返す

"""
ravelは参照を返却
flattenはコピーを返却
"""

print(a.dtype)
d = np.array([1,2],dtype=np.int16)
print(d.dtype)
print(d.astype(np.float16))


a = np.array([1, 2, 3])
b = np.array([[1,2,3],[4,5,6]])
print(a[0])
print(a[1:])
print(a[-1])
print(b[0])
print(b[1,0])
print(b[:,2])
print(b[1,:])
print(b[0,1:])
print(b[:,[0,2]])

print(end='\n')

print(a)
a[2] = 4
print(a)
print(b)
b[1,2] = 7
print(b)
b[:,2]=8
print(b)

a1 = a
a1[1] = 5
print(a1)
print(a)
a2 = a.copy()
a2[0] = 6
print(a2)
print(a)

c3 = c2.ravel()
c4 = c2.flatten()
print(c3)
print(c4)
c3[0] = 6
c4[1] = 7
print(c3)
print(c4)
print(c2)

"""
乱数
"""
f = np.random.random((3,2))
print(f) # <<< 0以上1未満のランダムな要素を持つ3×2行列を生成
f = np.random.rand(4,2)
print(f) # <<< 2つの引数を渡して、以上1未満のランダムな要素を持つ3×2行列を生成
f = np.random.randint(1, 10)
print(f) # <<< ある範囲内の任意の整数を生成
f = np.random.randint(1, 10, (3,2))
print(f) # <<< 1以上10未満のランダムな整数を要素に持つ3×2行列の2次元配列を生成
f = np.random.uniform(0.0, 5.0, size=(2,3))
print(f) # <<< 0.0以上5.0未満のランダムな小数値を要素に持つ2×3行列の2次元配列を生成
f = np.random.uniform(size=(4,3))
print(f) # <<< 0.0以上1.0未満のランダムな小数値を要素に持つ4×3行列の2次元配列
f = np.random.randn(4, 2)
print(f)

"""
連結
"""
print(np.concatenate([a, a1]))
b1 = np.array([[10], [20]])

print(np.concatenate([b, b1], axis=1))
print(np.hstack([b,b1]))
# <<< hstackと、concatenate(axis=1)は同義

b2 = np.array([30, 60, 45])
b3 = np.vstack([b, b2])
print(b3)

"""
分割
"""
first, second = np.hsplit(b3, [2])
# <<< 1つめの配列が2列、2つめが1列
print(first)
print(second)

first1, second1 = np.vsplit(b3, [2])
# <<< 1つめの配列が2行、2つめが1行
print(first1)
print(second1)

"""
次元追加
"""
print(a)
print(a[np.newaxis,:]) # <<< 行方向に次元を追加
print(a[:,np.newaxis]) # <<< 列方向に次元を追加

"""
グリッドデータの生成
"""
m = np.arange(0,4)
n = np.arange(4,7)
xx,yy = np.meshgrid(m,n)
print(xx)
print(yy)

"""
ユニバーサルファンクション
"""
li = [[-3, -2, -1], [0, 1, 2]]
new = []
for i, j in enumerate(li) :
    new.append([])
    for k in j :
        new[i].append(abs(k))
new
print(new)
print(np.abs(b))

print(end='\n')

"""
ブロードキャスト
"""
a = np.array([0, 1, 2])
print(a+10)
b = np.array([[-3, -2, -1],[0, 1, 2]])
print(a + b)
a1 = a[:,np.newaxis]
print(a1)
print(a + a1) # <<< 1次元配列aが、3行に拡張され、3×1行列の2次元配列が3×3行列に拡張されて足し算される