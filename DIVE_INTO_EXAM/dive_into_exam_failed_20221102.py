import numpy as np
import pandas as pd

m = np.arange(4)
n = np.arange(4)
print(m, end='\n\n')
print(n, end='\n\n')
xx,yy = np.meshgrid(m,n)
print(np.meshgrid(m,n), end='\n\n')
print(xx, end='\n\n')
print(yy, end='\n\n')

df = pd.DataFrame({"国名":["日本","アメリカ","イタリア","フランス","ロシア","ブラジル","イギリス"], "人口/万人":[12700, 328000,6000,6700,14500,20900,6600]})
print(df, end='\n\n')

# 人口/万人カラムを削除
df_droped = df.drop("人口/万人", axis=1)
print(df_droped, end='\n\n')
"""
実行結果
     国名
0    日本
1  アメリカ
2  イタリア
3  フランス
4   ロシア
5  ブラジル
6  イギリス
"""

A = np.eye(4)
print(A, end='\n\n')
first, second = np.hsplit(A, [2])
print(np.hsplit(A, [2]), end='\n\n')
print(first, end='\n\n')
"""
実行結果
[[1. 0.]
 [0. 1.]
 [0. 0.]
 [0. 0.]]
"""