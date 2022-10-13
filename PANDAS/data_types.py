import pandas as pd
import numpy as np

df = pd.read_excel("data/201704health.xlsx")

print(df.dtypes)
"""
日付がobjectになっている
これは、文字列として日付カラムが扱われている
ということ
"""

# applyメソッド
df.loc[:, 'date'] = df.loc[:, '日付'].apply(pd.to_datetime)
print(df.loc[:, "date"])

# astypeメソッド
df.loc[:, "摂取カロリー"] = df.loc[:, "摂取カロリー"].astype(np.float32)
df = df.set_index("date")
print(df.head())
