import numpy as np  # numpyをインポート
import pandas as pd
from pyparsing import col  # pandasをインポート

### Series ###
print("### Series ###", end="\n")

# 1次元データを指す
# Seriesオブジェクトを生成するには
# Seriesを使う
ser = pd.Series([10, 20, 30, 40])
print(ser, end="\r\n")
"""
実行結果
0    10
1    20
2    30
3    40
dtype: int64
"""

### DataFrame ###
print("### DataFrame ###", end="\n")

# 2次元のデータを指す
# DataFrameオブジェクトを生成するには
# DataFrameを使う
df = pd.DataFrame(
    [[10, "a", True], [20, "b", False], [30, "c", False], [40, "d", True]]
)
print(df, end="\n")
"""
実行結果
    0  1      2  
0  10  a   True  
1  20  b  False  
2  30  c  False  
3  40  d   True
"""

### DataFrameの概要を見る ###
print("### DataFrameの概要を見る ###", end="\n")

df = pd.DataFrame(np.arange(100).reshape((25, 4)))
print(df, end="\n")

# headメソッド
# DataFrameの先頭5行のみ出力
print(df.head(), end="\n")
"""
実行結果
    0   1   2   3
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
4  16  17  18  19
"""

# tailメソッド
# DataFrameの末尾5行のみ出力
print(df.tail(), end="\n")
"""
実行結果
     0   1   2   3
20  80  81  82  83
21  84  85  86  87
22  88  89  90  91
23  92  93  94  95
24  96  97  98  99
"""

# shape属性
# DataFrameのサイズを出力
print(df.shape, end="\n")
"""
実行結果
(25, 4)
"""

### インデックス名、カラム名 ###
print("### インデックス名、カラム名 ###", end="\n")
df = pd.DataFrame(np.arange(6).reshape((3, 2)))

df.index = ["01", "02", "03"]
df.columns = ["A", "B"]
print(df, end="\n")

named_df = pd.DataFrame(
    np.arange(6).reshape((3, 2)), columns=["A", "B"], index=["1行目", "2行目", "3行目"]
)
print(named_df, end="\n")
"""
実行結果
       A  B
1行目  0  1
2行目  2  3
3行目  4  5
"""

### データの抽出 ###
print("### データの抽出 ###", end="\n\n")

df = pd.DataFrame(
    np.arange(12).reshape((4, 3)),
    columns=["A", "B", "C"],
    index=["1行目", "2行目", "3行目", "4行目"],
)

# カラム名を直接指定して抽出
print(df["A"], end="\n")
"""
実行結果
1行目    0
2行目    3
3行目    6
4行目    9
Name: A, dtype: int32
"""

# 複数のカラムを取得
print(df[["A", "B"]], end="\n")
"""
実行結果
     A   B
1行目  0   1
2行目  3   4
3行目  6   7
4行目  9  10
"""

# インデックス値を指定しデータを抽出
print(df[:2], end="\n")
"""
実行結果
     A  B  C
1行目  0  1  2
2行目  3  4  5
"""

# DataFrameのすべてを出力
print(df.loc[:, :], end="\n")
"""
実行結果
     A   B   C
1行目  0   1   2
2行目  3   4   5
3行目  6   7   8
4行目  9  10  11
"""

# DataFrameのすべてを出力
print(df.loc[:, :], end="\n")
"""
実行結果
     A   B   C
1行目  0   1   2
2行目  3   4   5
3行目  6   7   8
4行目  9  10  11
"""

# すべてのインデックス方向の要素を出力
# locの1つ目の値にすべての要素を表す記号：を指定
print(df.loc[:, "A"], end="\n")
"""
実行結果
1行目    0
2行目    3
3行目    6
4行目    9
Name: A, dtype: int32
"""

# 複数のカラムを抽出する方法
print(df.loc[:, ["A", "B"]], end="\n")
"""
実行結果
     A   B
1行目  0   1
2行目  3   4
3行目  6   7
4行目  9  10
"""

### データの整形 ###
print("### データの整形 ###", end="\n\n")

df = pd.read_excel("data/201704health.xlsx")
print(df, end="\n")
"""
実行結果
            日付     歩数  摂取カロリー
0   2017-04-01   5439    2500
1   2017-04-02   2510    2300
2   2017-04-03  10238    1950
3   2017-04-04   8209    1850
4   2017-04-05   9434    1930
5   2017-04-06   7593    1800
6   2017-04-07   9320    1940
7   2017-04-08   4873    2300
8   2017-04-09  12045    1950
9   2017-04-10   7493    1850
10  2017-04-11   7289    1930
11  2017-04-12   6481    2300
12  2017-04-13  10287    1800
13  2017-04-14   8043    1940
14  2017-04-15   7435    2300
15  2017-04-16   7529    2300
16  2017-04-17   8031    1940
17  2017-04-18   8475    2300
18  2017-04-19   8132    1950
19  2017-04-20  15328    1800
20  2017-04-21  12849    1940
21  2017-04-22   4029    2300
22  2017-04-23   3890    1950
23  2017-04-24   8093    1850
24  2017-04-25   7823    1950
25  2017-04-26   7492    1850
26  2017-04-27   7203    1930
27  2017-04-28   7302    1850
28  2017-04-29   6033    2300
29  2017-04-30   4093    1950
"""

# 条件で抽出する
# 10,000歩以上の日のみを抽出
print(df["歩数"] >= 10000, end="\n")
"""
実行結果
0     False
1     False
2      True
3     False
4     False
5     False
6     False
7     False
8      True
9     False
10    False
11    False
12     True
13    False
14    False
15    False
16    False
17    False
18    False
19     True
20     True
21    False
22    False
23    False
24    False
25    False
26    False
27    False
28    False
29    False
Name: 歩数, dtype: bool
"""

# bool型のSeriesをDataFrameに当てはめる
df_selected = df[df["歩数"] >= 10000]
print(df_selected, end="\n")
"""
実行結果
            日付     歩数  摂取カロリー
2   2017-04-03  10238    1950
8   2017-04-09  12045    1950
12  2017-04-13  10287    1800
19  2017-04-20  15328    1800
20  2017-04-21  12849    1940
"""

# queryメソッド
# 条件を指定してデータを抽出する
print(df.query("歩数 >= 10000 and 摂取カロリー <= 1800"), end="\n")
"""
実行結果
            日付     歩数  摂取カロリー
12  2017-04-13  10287    1800
19  2017-04-20  15328    1800
"""

### データ型変換 ###
print("### データ型変換 ###", end="\n\n")

# dtypes
# 現在のデータ型を確認する
print(df.dtypes, end="\n")
"""
実行結果
日付        object
歩数         int64
摂取カロリー     int64
dtype: object
"""

# applyメソッド
# データを変換し指定カラムに挿入
df.loc[:, "date"] = df.loc[:, "日付"].apply(pd.to_datetime)
print(df.loc[:, "date"], end="\n")
"""
実行結果
0    2017-04-01
1    2017-04-02
2    2017-04-03
3    2017-04-04
4    2017-04-05
5    2017-04-06
6    2017-04-07
7    2017-04-08
8    2017-04-09
9    2017-04-10
10   2017-04-11
11   2017-04-12
12   2017-04-13
13   2017-04-14
14   2017-04-15
15   2017-04-16
16   2017-04-17
17   2017-04-18
18   2017-04-19
19   2017-04-20
20   2017-04-21
21   2017-04-22
22   2017-04-23
23   2017-04-24
24   2017-04-25
25   2017-04-26
26   2017-04-27
27   2017-04-28
28   2017-04-29
29   2017-04-30
Name: date, dtype: datetime64[ns]
"""

# astype
# 摂取カロリーをastypeメソッドを使いfloat型に変換
df.loc[:, "摂取カロリー"] = df.loc[:, "摂取カロリー"].astype(np.float32)

# set_index
# インデックスにdateカラムの値を設定
df = df.set_index("date")

print(df.head(), end="\n")
"""
実行結果
                    日付     歩数  摂取カロリー
date
2017-04-01  2017-04-01   5439  2500.0
2017-04-02  2017-04-02   2510  2300.0
2017-04-03  2017-04-03  10238  1950.0
2017-04-04  2017-04-04   8209  1850.0
2017-04-05  2017-04-05   9434  1930.0
"""

### 並べ替え ###
print("### 並べ替え ###", end="\n\n")

# sort_valuesメソッド
# デフォルトで昇順で並べ替えが行われる
print(df.sort_values(by="歩数"), end="\n")
"""
実行結果
                    日付     歩数  摂取カロリー
date
2017-04-02  2017-04-02   2510  2300.0
2017-04-23  2017-04-23   3890  1950.0
2017-04-22  2017-04-22   4029  2300.0
2017-04-30  2017-04-30   4093  1950.0
2017-04-08  2017-04-08   4873  2300.0
2017-04-01  2017-04-01   5439  2500.0
2017-04-29  2017-04-29   6033  2300.0
2017-04-12  2017-04-12   6481  2300.0
2017-04-27  2017-04-27   7203  1930.0
2017-04-11  2017-04-11   7289  1930.0
2017-04-28  2017-04-28   7302  1850.0
2017-04-15  2017-04-15   7435  2300.0
2017-04-26  2017-04-26   7492  1850.0
2017-04-10  2017-04-10   7493  1850.0
2017-04-16  2017-04-16   7529  2300.0
2017-04-06  2017-04-06   7593  1800.0
2017-04-25  2017-04-25   7823  1950.0
2017-04-17  2017-04-17   8031  1940.0
2017-04-14  2017-04-14   8043  1940.0
2017-04-24  2017-04-24   8093  1850.0
2017-04-19  2017-04-19   8132  1950.0
2017-04-04  2017-04-04   8209  1850.0
2017-04-18  2017-04-18   8475  2300.0
2017-04-07  2017-04-07   9320  1940.0
2017-04-05  2017-04-05   9434  1930.0
2017-04-03  2017-04-03  10238  1950.0
2017-04-13  2017-04-13  10287  1800.0
2017-04-09  2017-04-09  12045  1950.0
2017-04-21  2017-04-21  12849  1940.0
2017-04-20  2017-04-20  15328  1800.0
"""

# 降順で出力
# sort_valuesの引数にascending=Falseを設定
print(df.sort_values(by="歩数", ascending=False).head(), end="\n")
"""
実行結果
                    日付     歩数  摂取カロリー
date
2017-04-20  2017-04-20  15328  1800.0
2017-04-21  2017-04-21  12849  1940.0
2017-04-09  2017-04-09  12045  1950.0
2017-04-13  2017-04-13  10287  1800.0
2017-04-03  2017-04-03  10238  1950.0
"""

### 不要なカラムの削除 ###
print("### 不要なカラムの削除 ###", end="\n\n")

df = df.drop("日付", axis=1)
print(df.tail(), end="\n")
"""
実行結果
              歩数  摂取カロリー
date
2017-04-26  7492  1850.0
2017-04-27  7203  1930.0
2017-04-28  7302  1850.0
2017-04-29  6033  2300.0
2017-04-30  4093  1950.0
"""

### 組み合わせデータの挿入 ###
print("### 組み合わせデータの挿入 ###", end="\n\n")

# 歩数を摂取カロリーで割った値を、歩数/カロリーというカラムに挿入
df.loc[:, "歩数/カロリー"] = df.loc[:, "歩数"] / df.loc[:, "摂取カロリー"]
print(df, end="\n")
"""
実行結果
               歩数  摂取カロリー   歩数/カロリー
date
2017-04-01   5439  2500.0  2.175600
2017-04-02   2510  2300.0  1.091304
2017-04-03  10238  1950.0  5.250256
2017-04-04   8209  1850.0  4.437297
2017-04-05   9434  1930.0  4.888083
2017-04-06   7593  1800.0  4.218333
2017-04-07   9320  1940.0  4.804124
2017-04-08   4873  2300.0  2.118696
2017-04-09  12045  1950.0  6.176923
2017-04-10   7493  1850.0  4.050270
2017-04-11   7289  1930.0  3.776684
2017-04-12   6481  2300.0  2.817826
2017-04-13  10287  1800.0  5.715000
2017-04-14   8043  1940.0  4.145876
2017-04-15   7435  2300.0  3.232609
2017-04-16   7529  2300.0  3.273478
2017-04-17   8031  1940.0  4.139691
2017-04-18   8475  2300.0  3.684783
2017-04-19   8132  1950.0  4.170256
2017-04-20  15328  1800.0  8.515556
2017-04-21  12849  1940.0  6.623196
2017-04-22   4029  2300.0  1.751739
2017-04-23   3890  1950.0  1.994872
2017-04-24   8093  1850.0  4.374595
2017-04-25   7823  1950.0  4.011795
2017-04-26   7492  1850.0  4.049730
2017-04-27   7203  1930.0  3.732124
2017-04-28   7302  1850.0  3.947027
2017-04-29   6033  2300.0  2.623043
2017-04-30   4093  1950.0  2.098974
"""