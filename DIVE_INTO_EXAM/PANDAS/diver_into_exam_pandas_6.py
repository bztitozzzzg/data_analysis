from traceback import print_tb
import numpy as np
import pandas as pd

sales_df = pd.read_csv("data/sales_data.csv", index_col="日付", parse_dates=True)
weather_df = pd.read_csv("data/weather_data.csv",
                         index_col="日付", parse_dates=True)
february_df = pd.read_csv(
    "data/february_data.csv", index_col="日付", parse_dates=True)

print(sales_df)
"""
実行結果
              売り上げ   客数   客単価
日付
2021-01-01  549342  125  4395
2021-01-02  577869  150  3852
2021-01-03  328030  184  1783
2021-01-04  317730  156  2037
2021-01-05  492476  149  3305
2021-01-06  494278  112  4413
2021-01-07  446449  118  3783
2021-01-08  429130  181  2371
2021-01-09  346203  101  3428
2021-01-10  520374  151  3446
2021-01-11  453313  144  3148
2021-01-12  365632  148  2470
2021-01-13  549903  156  3525
2021-01-14  418857  191  2193
2021-01-15  371200  149  2491
2021-01-16  464782  186  2499
2021-01-17  496719  103  4823
2021-01-18  532857  167  3191
2021-01-19  335662  111  3024
2021-01-20  527748  121  4362
2021-01-21  430256  189  2276
2021-01-22  457698  198  2312
2021-01-23  545799  103  5299
2021-01-24  514338  111  4634
2021-01-25  330255  103  3206
2021-01-26  306648  194  1581
2021-01-27  519069  106  4897
2021-01-28  585872  109  5375
2021-01-29  383079  187  2049
2021-01-30  566339  114  4968
2021-01-31  564572  183  3085
"""

print(weather_df)
"""
実行結果
            気温 天気
日付
2021-01-01  22  曇
2021-01-02  20  晴
2021-01-03  23  雨
2021-01-04  23  曇
2021-01-05  18  雨
2021-01-06  15  晴
2021-01-07  15  曇
2021-01-08  22  晴
2021-01-09  17  晴
2021-01-10  18  晴
2021-01-11  19  晴
2021-01-12  23  雨
2021-01-13  18  雨
2021-01-14  21  晴
2021-01-15  16  曇
2021-01-16  16  曇
2021-01-17  16  雨
2021-01-18  22  雨
2021-01-19  23  晴
2021-01-20  15  雨
2021-01-21  17  晴
2021-01-22  15  晴
2021-01-23  15  曇
2021-01-24  20  雨
2021-01-25  24  雨
2021-01-26  24  雨
2021-01-27  23  晴
2021-01-28  21  雨
2021-01-29  19  晴
2021-01-30  15  晴
2021-01-31  23  曇
"""
print(february_df)
"""
実行結果
              売り上げ   客数   客単価  気温 天気
日付
2021-02-01  360547  127  2839  15  曇
2021-02-02  307686  102  3017  16  曇
2021-02-03  581181  171  3399  19  晴
2021-02-04  551938  167  3305  21  晴
2021-02-05  573605  117  4903  24  曇
2021-02-06  458212  173  2649  19  晴
2021-02-07  400408  126  3178  24  晴
2021-02-08  578027  171  3380  22  雨
2021-02-09  306488  121  2533  19  曇
2021-02-10  595903  158  3772  15  雨
2021-02-11  476045  172  2768  19  雨
2021-02-12  402068  176  2284  21  晴
2021-02-13  501486  167  3003  23  曇
2021-02-14  511853  159  3219  24  雨
2021-02-15  422749  102  4145  21  曇
2021-02-16  505571  158  3200  21  晴
2021-02-17  540856  139  3891  24  曇
2021-02-18  514593  173  2975  23  曇
2021-02-19  479182  103  4652  21  雨
2021-02-20  365749  185  1977  22  雨
2021-02-21  382602  157  2437  22  晴
2021-02-22  526799  100  5268  21  曇
2021-02-23  413624  122  3390  19  雨
2021-02-24  414459  196  2115  17  晴
2021-02-25  565849  186  3042  16  雨
2021-02-26  429201  180  2384  15  晴
2021-02-27  430954  109  3954  20  曇
2021-02-28  367642  144  2553  19  晴
"""

print(end='\n')

# DataFrameの連結（concat関数）
df = pd.concat([sales_df, weather_df], axis=1)
df
print(df)
"""
実行結果
              売り上げ   客数   客単価  気温 天気
日付
2021-01-01  549342  125  4395  22  曇
2021-01-02  577869  150  3852  20  晴
2021-01-03  328030  184  1783  23  雨
2021-01-04  317730  156  2037  23  曇
2021-01-05  492476  149  3305  18  雨
2021-01-06  494278  112  4413  15  晴
2021-01-07  446449  118  3783  15  曇
2021-01-08  429130  181  2371  22  晴
2021-01-09  346203  101  3428  17  晴
2021-01-10  520374  151  3446  18  晴
2021-01-11  453313  144  3148  19  晴
2021-01-12  365632  148  2470  23  雨
2021-01-13  549903  156  3525  18  雨
2021-01-14  418857  191  2193  21  晴
2021-01-15  371200  149  2491  16  曇
2021-01-16  464782  186  2499  16  曇
2021-01-17  496719  103  4823  16  雨
2021-01-18  532857  167  3191  22  雨
2021-01-19  335662  111  3024  23  晴
2021-01-20  527748  121  4362  15  雨
2021-01-21  430256  189  2276  17  晴
2021-01-22  457698  198  2312  15  晴
2021-01-23  545799  103  5299  15  曇
2021-01-24  514338  111  4634  20  雨
2021-01-25  330255  103  3206  24  雨
2021-01-26  306648  194  1581  24  雨
2021-01-27  519069  106  4897  23  晴
2021-01-28  585872  109  5375  21  雨
2021-01-29  383079  187  2049  19  晴
2021-01-30  566339  114  4968  15  晴
2021-01-31  564572  183  3085  23  曇
"""

print(end='\n')

# 行連結
df = pd.concat([df, february_df], axis=0)
df
print(df)
"""
実行結果
             売り上げ   客数   客単価  気温 天気
日付
2021-01-01  549342  125  4395  22  曇
2021-01-02  577869  150  3852  20  晴
2021-01-03  328030  184  1783  23  雨
2021-01-04  317730  156  2037  23  曇
2021-01-05  492476  149  3305  18  雨
2021-01-06  494278  112  4413  15  晴
2021-01-07  446449  118  3783  15  曇
2021-01-08  429130  181  2371  22  晴
2021-01-09  346203  101  3428  17  晴
2021-01-10  520374  151  3446  18  晴
2021-01-11  453313  144  3148  19  晴
2021-01-12  365632  148  2470  23  雨
2021-01-13  549903  156  3525  18  雨
2021-01-14  418857  191  2193  21  晴
2021-01-15  371200  149  2491  16  曇
2021-01-16  464782  186  2499  16  曇
2021-01-17  496719  103  4823  16  雨
2021-01-18  532857  167  3191  22  雨
2021-01-19  335662  111  3024  23  晴
2021-01-20  527748  121  4362  15  雨
2021-01-21  430256  189  2276  17  晴
2021-01-22  457698  198  2312  15  晴
2021-01-23  545799  103  5299  15  曇
2021-01-24  514338  111  4634  20  雨
2021-01-25  330255  103  3206  24  雨
2021-01-26  306648  194  1581  24  雨
2021-01-27  519069  106  4897  23  晴
2021-01-28  585872  109  5375  21  雨
2021-01-29  383079  187  2049  19  晴
2021-01-30  566339  114  4968  15  晴
2021-01-31  564572  183  3085  23  曇
2021-02-01  360547  127  2839  15  曇
2021-02-02  307686  102  3017  16  曇
2021-02-03  581181  171  3399  19  晴
2021-02-04  551938  167  3305  21  晴
2021-02-05  573605  117  4903  24  曇
2021-02-06  458212  173  2649  19  晴
2021-02-07  400408  126  3178  24  晴
2021-02-08  578027  171  3380  22  雨
2021-02-09  306488  121  2533  19  曇
2021-02-10  595903  158  3772  15  雨
2021-02-11  476045  172  2768  19  雨
2021-02-12  402068  176  2284  21  晴
2021-02-13  501486  167  3003  23  曇
2021-02-14  511853  159  3219  24  雨
2021-02-15  422749  102  4145  21  曇
2021-02-16  505571  158  3200  21  晴
2021-02-17  540856  139  3891  24  曇
2021-02-18  514593  173  2975  23  曇
2021-02-19  479182  103  4652  21  雨
2021-02-20  365749  185  1977  22  雨
2021-02-21  382602  157  2437  22  晴
2021-02-22  526799  100  5268  21  曇
2021-02-23  413624  122  3390  19  雨
2021-02-24  414459  196  2115  17  晴
2021-02-25  565849  186  3042  16  雨
2021-02-26  429201  180  2384  15  晴
2021-02-27  430954  109  3954  20  曇
2021-02-28  367642  144  2553  19  晴
"""

print(end='\n')

# maxメソッド（最大値確認）
df.loc[:, "客数"].max()
print(df.loc[:, "客数"].max())
"""
実行結果
198
"""

print(end='\n')

# minメソッド（最小値確認）
df.loc[:, "売り上げ"].min()
print(df.loc[:, "売り上げ"].min())
"""
実行結果
306488
"""

print(end='\n')

# meanメソッド（平均値）
df.loc[:, "客単価"].mean()
print(df.loc[:, "客単価"].mean())
"""
実行結果
3295.813559322034
"""

print(end='\n')

# medianメソッド（中央値）
df.loc[:, "売り上げ"].median()
print(df.loc[:, "売り上げ"].median())
"""
実行結果
464782.0
"""

print(end='\n')

# modeメソッド（最頻値）
df.loc[:, "天気"].mode()
print(df.loc[:, "天気"].mode())
"""
実行結果
0    晴
Name: 天気, dtype: object
"""

print(end='\n')

# stdメソッド（標準偏差）
df.loc[:, "客単価"].std()
print(df.loc[:, "客単価"].std())
"""
実行結果
972.2175589249252
"""
print(end='\n')
df.loc[:, "客単価"].std(ddof=0)
print(df.loc[:, "客単価"].std(ddof=0))
"""
実行結果
963.9432164613783
"""

print(end='\n')

# countメソッド（件数）
df[df.loc[:, "売り上げ"] >= 550000].count()
print(df[df.loc[:, "売り上げ"] >= 550000].count())
"""
実行結果
売り上げ    10
客数      10
客単価     10
気温      10
天気      10
dtype: int64
"""

print(end='\n')

# describeメソッド（要約統計量）
df.describe()
print(df.describe())
"""
実行結果
                売り上げ          客数          客単価         気温
count      59.000000   59.000000    59.000000  59.000000
mean   460809.423729  146.796610  3295.813559  19.661017
std     85798.149319   31.752154   972.217559   3.065999
min    306488.000000  100.000000  1581.000000  15.000000
25%    391743.500000  115.500000  2495.000000  17.000000
50%    464782.000000  150.000000  3191.000000  20.000000
75%    530302.500000  173.000000  3871.500000  22.000000
max    595903.000000  198.000000  5375.000000  24.000000
"""

print(end='\n')

# corrメソッド（相関関係）
df.corr()
print(df.corr())
"""
実行結果
          売り上げ        客数       客単価        気温
売り上げ  1.000000 -0.020908  0.637632 -0.085411
客数   -0.020908  1.000000 -0.757817  0.068527
客単価   0.637632 -0.757817  1.000000 -0.110313
気温   -0.085411  0.068527 -0.110313  1.000000
"""

print(end='\n')
print("#------------------------------------#", end='\n')
print("# 確認問題")

dates = pd.date_range(start="2021-01-01", end="2021-01-07")
df = pd.DataFrame([1, 10, 6, 9, 11, 10, 1000], index=dates)

df.median()
print(df.median())
"""
実行結果
0    10.0
dtype: float64
"""

print(end='\n')

dates = pd.date_range(start="2021-01-01", end="2021-01-07")
df = pd.DataFrame([1, 10, 6, 9, 11, 10, 1000], index=dates)

print((1+10+6+9+11+10+1000) / 7)
df.mean()
print(df.mean())
"""
実行結果
0    149.571429
dtype: float64
"""

print(end='\n')

dates = pd.date_range(start="2021-01-01", end="2021-01-07")
df = pd.DataFrame([1, 10, 6, 9, 11, 10, 1000], index=dates)

df.count() * df.mean() == df.sum()
print("df.count():", df.count())
print("df.mean():", df.mean())
print("df.sum():", df.sum())
print("df.count() * df.mean():=", df.count() * df.mean())
print(df.count() * df.mean() == df.sum())
"""
実行結果
0    True
dtype: bool
"""