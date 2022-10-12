from unicodedata import name
import numpy as np
import pandas as pd

# Seriesで1次元データ作成
ser = pd.Series([10, 20, 30, 40])
print("ser:=", ser, end='\n')

# 4 × 3行列のDataFrame
df = pd.DataFrame([[10, "a", True, ], [20, "b", False, ],
                  [30, "c", True, ], [40, "d", True, ]])
print("df:=", df, end='\n')

# 25 × 4行列のDataFrame
df = pd.DataFrame(np.arange(100).reshape((25, 4)))
print("df:=", df)

# headメソッド：DataFrameの先頭5行を抽出
print("head:=", df.head(), end='\n')

# tailメソッド：DataFrameの末尾5行を抽出
print("tail:=", df.tail(), end='\n')

# shapeメソッド：DataFrameのサイズ
print("shape:=", df.shape)

# インデックス名、カラム名
df = pd.DataFrame(np.arange(6).reshape((3, 2)))
print("df:=", df)

"""
インデックス名に文字列で、01から順に割り当てます。
カラム名には、Aから順番にアルファベットを割り当てます。
ここではインデックス名とカラム名を数値やアルファベットの順番に定義しました。
インデックス名及びカラム名は任意の文字列や数値などを指定することができます。
"""
df.index = ["01", "02", "03"]
df.columns = ["A", "B"]
print("df:=", df)

"""
DataFrame作成時に、インデックス名とカラム名をつける場合は
以下のように設定する
"""
named_df = pd.DataFrame(np.arange(6).reshape((3, 2)), columns=[
                        "A列", "B列"], index=["1行目", "2行目", "3行目"])
print("named_df:=", named_df)

# 辞書（dict）形式でDataFrameを作成
dict = pd.DataFrame({"A列": [0, 2, 4], "B列": [1, 3, 5]})
print("dict:=", dict)

# データの抽出
df = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=[
                  "A", "B", "C"], index=["1行目", "2行目", "3行目", "4行目"])
print("df:=", df)

print("df[""A""]:=\n", df["A"])
print("df[[""A"", ""B""]]:=", df[["A", "B"]])
print("df[:2]:=", df[:2])

print("df.loc[:,:]:=", df.loc[:, :])
print("df.loc[:, ""A""]:=", df.loc[:, "A"])
print("df.loc[:, [""A"", ""B""]]:=", df.loc[:, ["A", "B"]])
print("df.loc[""1行目"", :]:=", df.loc["1行目", :])
print("df.loc[[""1行目"",""3行目""], :]:=", df.loc[["1行目", "3行目"], :])
print("df.loc[[""1行目""],[""A"", ""C""]]:=", df.loc[["1行目"], ["A", "C"]])
