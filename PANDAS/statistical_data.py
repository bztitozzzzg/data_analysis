from django.forms import inlineformset_factory
import matplotlib
import pandas as pd
df = pd.read_pickle("data/df_201704health.pickle")

# 基本統計量
"""
各基本的統計量を出力
maxメソッドを使って最大値を確認
"""
print(df.loc[:, "摂取カロリー"].max())

"""
minメソッドを使って最小値を確認
"""
print(df.loc[:, "摂取カロリー"].min())

"""
modeメソッドを使って最頻値を確認
"""
print(df.loc[:, "摂取カロリー"].mode())

"""
meanメソッドを使って平均値を確認
"""
print(df.loc[:, "摂取カロリー"].mean())

"""
medianメソッドを使って中央値を確認
"""
print(df.loc[:, "摂取カロリー"].median())

"""
stdメソッドを使って標準偏差を確認
"""
print(df.loc[:, "摂取カロリー"].std())

"""
母集団の標準偏差を出力する場合は
stdメソッドにddof=0を指定
"""
print(df.loc[:, "摂取カロリー"].std(ddof=0))

"""
countメソッドを使って件数を確認
"""
print(df[df.loc[:, "摂取カロリー"] == 2300].count())

"""
要約
DataFrameの統計量をまとめて出力する方法
"""
# describeメソッド
print(df.describe())

"""
相関係数
カラム間のデータの関係を数値で確認
"""
print(df.corr())

"""
散布図行列
カラムごとのデータの関係をグラフで確認
Jupiter Notebookで確認
"""
