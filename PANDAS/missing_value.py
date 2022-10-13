"""
欠損値とは、NaNと表示されるデータが入っていない項目。
欠損値が存在すると、誤った計算結果や予期せぬ計算結果になる場合がある
そのため、欠損値を処理しておく必要がある
"""
import pandas as pd
df_201705 = pd.read_csv("data/201705health.csv",
                        encoding="utf-8", index_col='日付', parse_dates=True)
print(df_201705)

# dropnaメソッド：欠損値を削除
df_201705_drop = df_201705.dropna()
print(df_201705_drop)

# fillnaメソッド：欠損値に0を代入
df_201705_fillna = df_201705.fillna(0)
print(df_201705_fillna)

# fillnaメソッドにmethod='ffill'を与えて
# 欠損値を1つ手前の値で補完
df_201705_fill = df_201705.fillna(method='ffill')
print(df_201705_fill)

# 平均値、中央値、最頻値で欠損値を補完
# 平均値
df_201705_fillmean = df_201705.fillna(df_201705.mean())
print(df_201705_fillmean)

# 中央値
df_201705_fillmedian = df_201705.fillna(df_201705.median())
print(df_201705_fillmedian)

# 最頻値
df_201705_fillmode = df_201705.fillna(df_201705.mode().iloc[0, :])
print(df_201705_fillmode)
