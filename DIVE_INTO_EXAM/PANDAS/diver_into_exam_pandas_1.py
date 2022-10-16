import pandas as pd

# Series
row = pd.Series([10, 20, 30, 40, 50])
print(row)
"""
実行結果
0    10
1    20
2    30
3    40
4    50
dtype: int64
"""

print(end='\n')

# DataFrameの作成
df = pd.DataFrame([[10, "ten", True],
                   [20, "twenty", False],
                   [30, "thirty", True],
                   [40, "forty", False],
                   [50, "fifty", False]])
print(df)
"""
実行結果
    0       1      2
0  10     ten   True
1  20  twenty  False
2  30  thirty   True
3  40   forty  False
4  50   fifty  False
"""
