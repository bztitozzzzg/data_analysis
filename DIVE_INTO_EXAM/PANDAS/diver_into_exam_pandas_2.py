import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(100).reshape((20, 5)))
print(df)
"""
実行結果
     0   1   2   3   4
0    0   1   2   3   4
1    5   6   7   8   9
2   10  11  12  13  14
3   15  16  17  18  19
4   20  21  22  23  24
5   25  26  27  28  29
6   30  31  32  33  34
7   35  36  37  38  39
8   40  41  42  43  44
9   45  46  47  48  49
10  50  51  52  53  54
11  55  56  57  58  59
12  60  61  62  63  64
13  65  66  67  68  69
14  70  71  72  73  74
15  75  76  77  78  79
16  80  81  82  83  84
17  85  86  87  88  89
18  90  91  92  93  94
19  95  96  97  98  99
"""

print(end='\n')

# headメソッド（先頭から任意のデータを行数分抽出）
print(df.head())
"""
実行結果
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
4  20  21  22  23  24
"""

print(end='\n')

print(df.head(10))
"""
実行結果
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
3  15  16  17  18  19
4  20  21  22  23  24
5  25  26  27  28  29
6  30  31  32  33  34
7  35  36  37  38  39
8  40  41  42  43  44
9  45  46  47  48  49
"""

print(end='\n')

# shapeメソッド（DataFrameのサイズ確認）
print(df.shape)
"""
実行結果
(20, 5)
"""

print(end='\n')

# インデックス名とカラム名を設定
df = pd.DataFrame(np.arange(9).reshape((3, 3)))
print(df)
"""
実行結果
   0  1  2
0  0  1  2
1  3  4  5
2  6  7  8
"""

print(end='\n')

# DataFrameのインデックス名を”1行目”、”2行目”、”3行目”、カラム名を”A列”、”B列”、”C列”に変更
df.index = ["1行目", "2行目", "3行目"]
df.columns = ["A列", "B列", "C列"]
print(df)
"""
実行結果
     A列  B列  C列
1行目   0   1   2
2行目   3   4   5
3行目   6   7   8
"""

print(end='\n')

df2 = pd.DataFrame(np.arange(9).reshape((3, 3)),
                   index=["1行目", "2行目", "3行目"],
                   columns=["A列", "B列", "C列"])
print(df2)
"""
実行結果
     A列  B列  C列
1行目   0   1   2
2行目   3   4   5
3行目   6   7   8
"""

print(end='\n')

# 辞書形式でのDataFrame作成
print(pd.DataFrame({"A列": [1, 2, 3], "B列": [
      10, 20, 30], "C列": [True, False, False]}))

"""
実行結果
   A列  B列     C列
0   1  10   True
1   2  20  False
2   3  30  False
"""

print(end='\n')

# データの抽出
df = pd.DataFrame(np.arange(20).reshape((5, 4)),
                  index=["1行目", "2行目", "3行目", "4行目", "5行目"],
                  columns=["A列", "B列", "C列", "D列"])
print(df)
"""
実行結果
     A列  B列  C列  D列
1行目   0   1   2   3
2行目   4   5   6   7
3行目   8   9  10  11
4行目  12  13  14  15
5行目  16  17  18  19
"""

print(end='\n')

# 列データをカラム名を指定して抽出
print(df["A列"])
"""
実行結果
1行目     0
2行目     4
3行目     8
4行目    12
5行目    16
Name: A列, dtype: int32
"""

print(end='\n')

# 複数の列データをカラム名を指定して抽出
print(df[["A列", "C列"]])
"""
実行結果
     A列  C列
1行目   0   2
2行目   4   6
3行目   8  10
4行目  12  14
5行目  16  18
"""

print(end='\n')

# 行データを抽出
print(df[:"1行目"])
"""
実行結果
     A列  B列  C列  D列
1行目   0   1   2   3
"""

print(end='\n')

# 先頭から指定した行までが抽出
print(df[:"3行目"])
"""
実行結果
     A列  B列  C列  D列
1行目   0   1   2   3
2行目   4   5   6   7
3行目   8   9  10  11
"""

print(end='\n')

# 開始位置と終了位置を指定
print(df["3行目":"3行目"])
"""
実行結果
     A列  B列  C列  D列
3行目   8   9  10  11
"""

print(end='\n')

# loc・ilocの使い方
df = pd.DataFrame(np.arange(20).reshape((5, 4)),
                  index=["1行目", "2行目", "3行目", "4行目", "5行目"],
                  columns=["A列", "B列", "C列", "D列"])
print(df)
"""
実行結果
     A列  B列  C列  D列
1行目   0   1   2   3
2行目   4   5   6   7
3行目   8   9  10  11
4行目  12  13  14  15
5行目  16  17  18  19
"""

print(end='\n')

# loc
# A列のデータを抽出
print(df.loc[:, "A列"])
"""
実行結果
1行目     0
2行目     4
3行目     8
4行目    12
5行目    16
Name: A列, dtype: int32
"""

print(end='\n')

# A列とC列のデータを抽出
print(df.loc[:, ["A列", "C列"]])
"""
実行結果
     A列  C列
1行目   0   2
2行目   4   6
3行目   8  10
4行目  12  14
5行目  16  18
"""

print(end='\n')

# 3行目のデータを抽出
print(df.loc["3行目", :])
"""
実行結果
A列     8
B列     9
C列    10
D列    11
Name: 3行目, dtype: int32
"""

print(end='\n')

# 2行目と4行目のデータを抽出
print(df.loc[["2行目", "4行目"], :])
"""
実行結果
     A列  B列  C列  D列
2行目   4   5   6   7
4行目  12  13  14  15
"""

print(end='\n')

# 2行目と5行目のB列とD列のデータを抽出
print(df.loc[["2行目", "5行目"], ["B列", "D列"]])
"""
実行結果
     B列  D列
2行目   5   7
5行目  17  19
"""

print(end='\n')

# iloc
# インデックス番号0のカラム番号2のデータを抽出
print(df.iloc[0, 2])
"""
実行結果
2
"""

print(end='\n')

# インデックス番号2以降のカラム番号3のデータを抽出
print(df.iloc[2:, 3])
"""
実行結果
3行目    11
4行目    15
5行目    19
Name: D列, dtype: int32
"""

print(end='\n')

# インデックス番号とカラム番号の両方で範囲を指定
print(df.iloc[1:, :2])
"""
実行結果
     A列  B列
2行目   4   5
3行目   8   9
4行目  12  13
5行目  16  17
"""

print(end='\n')
print("#------------------------------------#", end='\n')
print("# 確認問題")
df = pd.DataFrame(np.arange(9).reshape(3, 3))

# df.index = (A)
# df.columns = (B)
df.index = ["1~4月", "5~8月", "9~12月"]
df.columns = ["A社", "B社", "C社"]

print(df)
"""
実行結果
       A社  B社  C社
1~4月    0   1   2
5~8月    3   4   5
9~12月   6   7   8
(A):["1~4月", "5~8月", "9~12月"]
(B):["A社", "B社", "C社"]
"""

print(end='\n')

print(pd.DataFrame(np.arange(100).reshape(25, 4)).head())
# メソッドは、head()
"""
実行結果
    0   1   2   3
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
4  16  17  18  19
"""

print(end='\n')

A = {"商品名": ["apple", "orange", "banana"],
     "単価": [100, 150, 80], "在庫数": [10, 20, 100]}
print(pd.DataFrame(A))
"""
実行結果
      商品名   単価  在庫数
0   apple  100   10
1  orange  150   20
2  banana   80  100
"""

print(end='\n')

df = pd.DataFrame({"商品名": ["apple", "orange", "banana"], "単価": [
                  100, 150, 80], "在庫数": [10, 20, 100]})
A = df[["商品名", "在庫数"]]
print(A)
"""
実行結果
      商品名  在庫数
0   apple   10
1  orange   20
2  banana  100
"""

print(end='\n')

df = pd.DataFrame(np.arange(9).reshape(3, 3), index=[
                  "1~4月", "5~8月", "9~12月"], columns=["A社", "B社", "C社"])
A = df.loc[:, "B社"]
print(A)
"""
実行結果
1~4月     1
5~8月     4
9~12月    7
Name: B社, dtype: int32
"""
# df.loc[:, "列名"]
# [:, ["カラム名1", "カラム名2"]]

print(end='\n')

df = pd.DataFrame(np.arange(9).reshape(3, 3), index=[
                  "1~4月", "5~8月", "9~12月"], columns=["A社", "B社", "C社"])
print(df.loc["1~4月", "B社"])
"""
実行結果
1
"""

print(end='\n')

df = pd.DataFrame({"商品名": ["apple", "orange", "banana"], "単価": [
                  100, 150, 80], "在庫数": [10, 20, 100]})
df.loc[:, "合計値"] = df.loc[:, "単価"] * df.loc[:, "在庫数"]
print(df)
"""
実行結果
      商品名   単価  在庫数   合計値
0   apple  100   10  1000
1  orange  150   20  3000
2  banana   80  100  8000
"""
