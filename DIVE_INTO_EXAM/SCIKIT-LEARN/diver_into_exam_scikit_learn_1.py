from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
df = pd.DataFrame(
    {
        'A': [1, 2, 3, 4, np.nan],
        'B': [10, np.nan, 30, 40, 50],
        'C': [np.nan, 200, 300, 400, 500]
    }
)
df
print(df)
"""
実行結果
     A     B      C
0  1.0  10.0    NaN
1  2.0   NaN  200.0
2  3.0  30.0  300.0
3  4.0  40.0  400.0
4  NaN  50.0  500.0
"""

print(end='\n')

# 欠損値が含まれているかの確認（isnullメソッド）
df.isnull()
print(df.isnull())
"""
実行結果
       A      B      C
0  False  False   True
1  False   True  False
2  False  False  False
3  False  False  False
4   True  False  False
"""

print(end='\n')

# 欠損値の除外（dropnaメソッド）
df.dropna()
print(df.dropna())
"""
実行結果
     A     B      C
2  3.0  30.0  300.0
3  4.0  40.0  400.0
"""

print(end='\n')

imp = SimpleImputer(strategy='mean')
imp.fit(df)
print(imp.fit(df))
"""
実行結果
SimpleImputer()
"""

print(end='\n')

imp.transform(df)
print(imp.transform(df))
"""
実行結果
[[  1.   10.  350. ]
 [  2.   32.5 200. ]
 [  3.   30.  300. ]
 [  4.   40.  400. ]
 [  2.5  50.  500. ]]
"""

print(end='\n')
print('******ラベルエンコーディング******')
# ラベルエンコーディング
df = pd.DataFrame([[23, 'male'],
                   [43, 'female'],
                   [31, 'male'],
                   [35, 'female'],
                   [40, 'male']],
                  columns=['age', 'sex'])
df

le = LabelEncoder()
le.fit(df['sex'])
print(le.fit(df['sex']))
"""
実行結果
LabelEncoder()
"""
le.transform(df['sex'])
print(le.transform(df['sex']))
"""
実行結果
[1 0 1 0 1]
"""
le.classes_
print(le.classes_)
"""
実行結果
['female' 'male']
"""

print(end='\n')
print('******One-hotエンコーディング******')
df = pd.DataFrame([[23, 'male'],
                   [43, 'female'],
                   [31, 'male'],
                   [35, 'female'],
                   [40, 'male']],
                  columns=['age', 'sex'])
df
ohe = ColumnTransformer(
    [("OneHotEncoder", OneHotEncoder(), [1])], remainder='passthrough')
df_ohe = df.copy()
ohe.fit_transform(df_ohe)
print(ohe.fit_transform(df_ohe))
"""
実行結果
[[ 0.  1. 23.]
 [ 1.  0. 43.]
 [ 0.  1. 31.]
 [ 1.  0. 35.]
 [ 0.  1. 40.]]
"""

print(end='\n')
print('******特徴量の正規化******')
df = pd.DataFrame({
    'data1': [1, 2, 3, 4, 5],
    'data2': [1000, 3000, 3500, 5000, 7000]
})
df
scaler = StandardScaler()
scaler.fit_transform(df)
print(scaler.fit_transform(df))
"""
実行結果
[[-1.41421356 -1.44280393]
 [-0.70710678 -0.44776674]
 [ 0.         -0.19900744]
 [ 0.70710678  0.54727045]
 [ 1.41421356  1.54230764]]
"""

print(end='\n')
print('******最小最大正規化******')
scaler = MinMaxScaler()
scaler.fit_transform(df)
print(scaler.fit_transform(df))
"""
実行結果
[[0.         0.        ]
 [0.25       0.33333333]
 [0.5        0.41666667]
 [0.75       0.66666667]
 [1.         1.        ]]
"""
