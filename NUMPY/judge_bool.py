import numpy as np

a = np.arange(3)
print("a:", np.arange(3))
b = np.arange(-3, 3).reshape((2, 3))
print("b:", np.arange(-3, 3).reshape((2, 3)))
c = np.arange(1, 7).reshape((2, 3))
print("c:", np.arange(1, 7).reshape((2, 3)))


print("a > 1:", a > 1)


print("b > 0:", b > 0)

# np.count_nonzeroは、0でない要素数を出力
print("np.count_nonzero(b > 0):", np.count_nonzero(b > 0))

# np.sumは、要素の値全てを足す
print("np.sum(b > 0):", np.sum(b > 0))
print("np.sum(b):", np.sum(b))

# np.anyは要素の中にTrueが含まれているか否かを判定する
print("np.any(b > 0):", np.any(b > 0))  # 1つ以上のTrueがあれば、Trueを返却

# np.allは、全てがTrueか否かを判定する
print("np.all(b > 0):", np.all(b > 0))

# 真偽値配列を使って、条件に合致したものだけの要素を新たな配列として出力
# b: [[-3 -2 -1][ 0  1  2]]より、[1, 2]となる
print("b[b > 0]:", b[b > 0])


print("b == c:", b == c)

print("a == b", a == b)

# 複数の配列の比較を、ビット演算で行う
print("(b == c) | (a == b)", (b == c) | (a == b))

# 複数の配列の条件に合う要素のみを配列から取得
print("b[(b == c) | (a == b)]:", b[(b == c) | (a == b)])

# 配列同士が同じ要素で構成されているか確認
# ※全て同じか、というより、誤差の範囲、を見ている
print("np.allclose(b, c):", np.allclose(b, c))

# 絶対誤差:atolキーワード引数を使う
# atol=10は、誤差を10
print("np.allclose(b, c, atol=10):", np.allclose(b, c, atol=10))
