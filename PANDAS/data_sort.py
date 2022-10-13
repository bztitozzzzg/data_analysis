import pandas as pd
import numpy as np

df = pd.read_excel("data/201704health.xlsx")

# sort_valuesメソッド
# デフォルトで昇順で並べ替え
print(df.sort_values(by="歩数"))

# 降順に並べ替え
print(df.sort_values(by="歩数", ascending=False).head())

# 不要なカラムの削除
df = df.drop("日付", axis=1)
print(df.tail())
