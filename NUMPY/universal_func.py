"""
ユニバーサルファンクション
<p>
NumPyの強力なツールの１つ。
配列要素内のデータを一括で変換してくれる。
ここでは、配列要素の絶対値を返す
</p>
"""
import numpy as np

a = np.arange(3)
b = np.arange(-3, 3).reshape((2, 3))
c = np.arange(1, 7).reshape((2, 3))
d = np.arange(6).reshape((3, 2))
e = np.linspace(-1, 1, 10)

li = [[-3, -2, -1], [0, 1, 2]]
new = []

for i, j in enumerate(li):
    new.append([])
    for k in j:
        new[i].append(abs(k))

print("new:", new)
print("np.abs(b):", np.abs(b))  # abs関数
print("np.sin(e):", np.sin(e))  # sin関数
print("np.cos(e):", np.cos(e))  # cos関数
print("np.log(a):", np.log(a))  # ネイピア数を底とする自然対数logをlog関数にて計算
"""
np.log(a): [      -inf 0.         0.69314718]
-infは、マイナス無限大を意味する
"""
print("np.log10(c):", np.log10(c))  # 常用対数（logの底が10の時）
print("np.exp(a):", np.exp(a))
