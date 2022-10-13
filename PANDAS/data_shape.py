import pandas as pd
import numpy as np

df = pd.read_excel("data/201704health.xlsx")
print(df)

# 条件の抽出
# 10,000歩以上の日のみを抽出
# df.loc[:,"歩数"]>=10000と同じ
print(df["歩数"] >= 10000)

df_selected = df[df["歩数"] >= 10000]
print(df_selected)
print(df_selected.shape)  # 5 × 3行列のDataFrame

# queryメソッドでデータを抽出
print(df.query('歩数 >= 10000 and 摂取カロリー <= 1800'))
