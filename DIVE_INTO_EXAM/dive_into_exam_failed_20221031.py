import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})
print(df, end="\n\n")
print(df.iloc[1], end="\n\n")
print(df.iloc[1] > 3)
"""
実行結果
A    False
B     True
Name: 1, dtype: bool
df.iloc[1]は1次元目の2行目にアクセスします。
"""
