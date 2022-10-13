import pandas as pd
import numpy as np

# 1カ月分のデータを作成
dates = pd.date_range(start="2017-04-01", end="2017-04-30")
np.random.seed(123)
df = pd.DataFrame(np.random.randint(1, 31, 30), index=dates, columns=["乱数"])
print(df)

# 1年365日のデータを作成
dates = pd.date_range(start="2017-01-01", periods=365)
np.random.seed(123)
df = pd.DataFrame(np.random.randint(1, 31, 365), index=dates, columns=["乱数"])
print(df)

# 月平均のデータにする
# 365日分のデータを使って毎月の平均値を求める
print(df.groupby(pd.Grouper(freq='M')).mean())
"""
groupbyメソッドを使い、データのサマライズを行う。
引数にfreq='M'を指定。
Grouperは、周期的なグルーピングを行うことができる。
freq='M'とし、月ごとのデータにグルーピングするようにする
"""

# 引数のカラムを乱数に固定して
# resampleメソッドを使い
# 毎月の平均値を出力
print(df.loc[:, "乱数"].resample('M').mean())

# 複雑な条件のインデックス
# 1年分の土曜日の日付データの作り方を確認

print(pd.date_range(start="2017-01-01", end="2017-12-31", freq="W-SAT"))
df_year = pd.DataFrame(df.groupby(
    pd.Grouper(freq='W-SAT')).sum(), columns=['乱数'])
print(df_year)
