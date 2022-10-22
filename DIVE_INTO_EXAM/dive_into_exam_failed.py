import numpy as np  # NumPy
import pandas as pd  # pandas

A = np.array([0, 1, 2, 3, 4, 5])
B = np.array([6, 7, 8])
A2 = A.reshape(2, 3)  # <-- 2行3列に変換
print(A2)
print(end='\n')
B2 = B[np.newaxis, :]  # <-- 1つ次元を追加
print(B2)
print(end='\n')
np.vstack([A2, B2])
print(np.vstack([A2, B2]))
"""
実行結果
[[0 1 2]
 [3 4 5]
 [6 7 8]]

解説
vstackで列方向で結合しています。
ただ、その前にAはreshapeで2行3列の2次元配列に変換されているので、
Bもnewaxisを使って2次元の配列に変換している流れになります。
"""

print(end='\n')
A = np.full(10, 10.0)
B = np.array([10])*10
C = np.zeros(10)  # <-- 10個の要素がすべて0
C1 = C+10
D = np.ones(10)  # <-- 10この要素がすべて1
D1 = D*10
print('A=', A)
print('B=', B)
print('C=', C)
print('C1=', C1)
print('D=', D)
print('D1=', D1)
"""
実行結果
A= [10. 10. 10. 10. 10. 10. 10. 10. 10. 10.]
B= [100]
C= [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
C1= [10. 10. 10. 10. 10. 10. 10. 10. 10. 10.]
D= [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
D1= [10. 10. 10. 10. 10. 10. 10. 10. 10. 10.]
"""

print(end='\n')
df = pd.DataFrame([["日本", 38000], ["アメリカ", 9834000],
                  ["中国", 959700], ["イタリア", 301300]])
df.rename(columns={"name of country": "国名", "area": "面積"})
# <-- df.rename(columns={A:A', B:B'})
# <-- AをA'に、BをB'に変換するよ、という意味
print(df)
"""
実行結果
      0        1
0    日本    38000
1  アメリカ  9834000
2    中国   959700
3  イタリア   301300

解説
renameの引数にcolumnsを指定してdictもしくは関数を渡すことでカラム名を変更できます。
"""

print(end='\n')

a = np.array([[0, 1, 10], [0, 1, 10]])
print(a, end='\n')
b = a.copy()
print(b, end='\n')
# a2 = a.reshape(3, 2)
a2 = a
print(a2, end='\n')
print(b*a)
print(b*a2)
"""
実行結果
aの行列(2×3行列)
[[ 0  1 10]
 [ 0  1 10]]

bの行列(2×3行列)
[[ 0  1 10]
 [ 0  1 10]]

a2の行列(3×2行列)
[[ 0  1]
 [10  0]
 [ 1 10]]

ValueError: operands could not be broadcast together with shapes (2,3) (3,2)
同じ形状（行列）にしないと、ValueErrorとなってしまうため、NG.
"""

print(end='\n')

# pandasデータフレームdfをNumPy配列に変換する処理として正しいものを選べ
df = pd.DataFrame([["日本", 38000], ["アメリカ", 9834000],
                  ["中国", 959700], ["イタリア", 301300]])
df.values
print(df.values)
"""
実行結果
[['日本' 38000]
 ['アメリカ' 9834000]
 ['中国' 959700]
 ['イタリア' 301300]]
"""

print(end='\n')

A = np.linspace(0, 2, 5)  # <-- 0~2の範囲を均等に5等分する
print('A=', A, end='\n')
B = np.diff(A)*2  # <-- 要素の差分を2倍する
print('B=', B, end='\n')
B == np.ones(4)  # <-- np.ones(4)は要素すべて1の配列
print(B == np.ones(4))
"""
実行結果
[ True  True  True  True]

解説
NumPyのメソッドの問題です。
linespace()メソッドは要素数を指定する等差数列を生成するメソッドです。
Aは1行5列となり、0, 0.5, 1, 1.5, 2.0 となります。
diffメソッドは要素間の差を計算します。
Bにはこの差分を2倍した値がはいりますので、全て１が格納されます。
np.onesで全てが１の配列と同値になります。
"""
print(end='\n')
# matplotlibのhist()メソッドの返り値として取得できる情報として正しいもの
# <-- (各ビンの度数、各ビンの範囲、パッチオブジェクトが格納されている配列)の3つの返り値を持つ
print(end='\n')
# 配列の形状が(2,10)であり、各要素が平均2、標準偏差5の正規分布に従う乱数を生成するコマンドとして正しいもの
np.random.normal(2, 5, size=(2, 10))
print(np.random.normal(2, 5, size=(2, 10)))
"""
実行結果
[[ 8.62246688  5.46617593  1.88935155 -5.22715001  8.44466148  4.8629639
   0.83825981 -2.71920342  6.09091646 -5.37576231]
 [ 6.04653193 -3.02435653 10.12368393  2.23642654  5.36384716 -1.75378393
  -6.39510572 -2.58340917  0.56560899  1.00639036]]

解説
NumPyのrandomモジュールの問題です。
randomモジュールのnormalメソッドは
任意の平均と標準偏差を用いて正規分布に従う乱数を生成出来ます。
"""

print(end='\n')
print('******np.dot(a,b)を実行した場合の出力と同じにならないもの******')
a = np.array([[0, 1, 10], [0, 1, 10]])
b = a.copy()
a = a.reshape(3, 2)
print(a)
print(b)
# print('np.multiply(a, b):=', np.multiply(a, b)) <-- multiply(a, b)はNG
print('np.matmul(a, b):=', np.matmul(a, b))
print('a @ b:=', a @ b)
print('a.dot(b):=', a.dot(b))
"""
実行結果
np.matmul(a, b):= [[  0   1  10]
 [  0  10 100]
 [  0  11 110]]

a @ b:= [[  0   1  10]
 [  0  10 100]
 [  0  11 110]]

a.dot(b):= [[  0   1  10]
 [  0  10 100]
 [  0  11 110]]

解説
multiplyは引数の要素ごとに乗算します。
今回はbroadcastできないためエラーにもなります。
その他の選択肢は内積と行列積をおこなうメソッドであり, 
np.dot(a, b)を実行した場合の出力と同じ結果を得ます。
"""

print(end='\n')
A = np.eye(4)  # <-- 4×4の単位行列を作成
print('A:=', A)
first, second = np.vsplit(A, [3])  # <-- vsplitで4行目をsecondに入れる。
print('first:=', first)
print('second:=', second)
second.T
print(second.T)
"""
実行結果
[[0.]
 [0.]
 [0.]
 [1.]]
"""

print(end='\n')
A = np.eye(4)  # <-- 4×4の単位行列
first, second = np.hsplit(A, [2])  # <-- hsplitで3列目以降をsecondに入れる。
first
print('first:=', first)
print('second:=', second)
"""
実行結果
first:= [[1. 0.]
 [0. 1.]
 [0. 0.]
 [0. 0.]]
second:= [[0. 0.]
 [0. 0.]
 [1. 0.]
 [0. 1.]]

解説
NumPyのメソッドの問題です。
4行4列の単位行列を作成したあと、hsplitで0列~1列目までをfirstに入れます。
4行2列のデータになり、選択肢が正解になります。
"""

print(end='\n')

A = np.arange(10)
print('A:=', A)
A.reshape(5, 2)
print('A.reshape(5, 2):=', A.reshape(5, 2))
"""
実行結果
A:= [0 1 2 3 4 5 6 7 8 9]
A.reshape(5, 2):= [[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
"""

print(end='\n')
A = [1]*10
A
print('A:=', A)
"""
実行結果
A:= [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

解説
*は値を指定した回数繰り返して新しい値として出力します。
"""

print(end='\n')
print('******浅いコピーと深いコピー******')
A = np.array([[1, 2, 3], [4, 5, 6]])
B = A.ravel()
A[0, :] = 0
print('A:=', A)
B.reshape(3, 2)
print('B.reshape(3, 2):=', B.reshape(3, 2))
"""
実行結果
A:= [[0 0 0]
 [4 5 6]]
B.reshape(3, 2):= [[0 0]
 [0 4]
 [5 6]]

解説
浅いコピーである ravelメソッドを使用しているのでAの変更はBに影響
"""

print(end='\n')
A = np.array([[1, 2, 3], [4, 5, 6]])
B = A.flatten()  # Aの行列をBへコピー
A[1, :] = 0  # <-- 2行目をすべて0にする
print('A:=', A)
B[-1]
print('B[-1]:=', B[-1])
"""
実行結果
A:= [[1 2 3]
 [0 0 0]]
B[-1]:= 6
"""

print(end='\n')

A = np.array([[1, 2, 3], [4, 5, 6]])
B = A[0, :]  # <--BにAの1行目の要素すべてをコピー
A[0, :] = 0  # <--1行目の要素をすべて0にする
print('A:=', A)
B
print('B:=', B)
"""
実行結果
A:= [[0 0 0]
 [4 5 6]]
B:= [0 0 0]
"""
