"""
データの再呼び出し、DataFrameの連結
"""
import pandas as pd
import numpy as np

df = pd.read_pickle("data/df_201704health.pickle")
df_moved = pd.read_pickle("data/df_201704moved.pickle")

# 列方向のデータ連結
"""
2つのDataFrameを列方向（カラム方向）に連結
concat関数を使い、引数に2つのDataFrameをリストに渡す
axis=1を引数に加えることで、列方向の連結となる
"""

df_merged = pd.concat([df, df_moved], axis=1)
print(df_merged)

# 行方向のデータ連結
"""
2つのDataFrameを行方向（インデックス方向）に連結を行う
concat関数を使い、引数に2つのDataFrameをリストに渡す
axis=0を引数に加えることで、行方向の連結となる
"""
df_201705 = pd.read_csv("data/201705health.csv",
                        encoding="utf-8", index_col='日付', parse_dates=True)
df_201705_fill = df_201705.fillna(method='ffill')

df_merged_0405 = pd.concat([df_merged, df_201705_fill], axis=0, sort=True)
print(df_merged_0405)
