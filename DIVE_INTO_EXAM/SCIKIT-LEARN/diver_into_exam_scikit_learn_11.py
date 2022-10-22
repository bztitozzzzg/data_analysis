from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.DataFrame({"予測購入確率": np.array([0.99, 0.97, 0.91, 0.88, 0.82, 0.81, 0.79, 0.74, 0.65, 0.6, 0.53, 0.50, 0.41, 0.39, 0.33, 0.3, 0.25, 0.21, 0.18, 0.17]),
                   "実績": np.array([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0]),
                   "真陽性率": np.array([1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, 11, 12, 12])/12,
                   "偽陽性率": np.array([0, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8])/8})
df
print(df)
"""
実行結果
    予測購入確率  実績      真陽性率   偽陽性率
0     0.99   1  0.083333  0.000
1     0.97   0  0.083333  0.125
2     0.91   1  0.166667  0.125
3     0.88   0  0.166667  0.250
4     0.82   1  0.250000  0.250
5     0.81   0  0.250000  0.375
6     0.79   0  0.250000  0.500
7     0.74   1  0.333333  0.500
8     0.65   1  0.416667  0.500
9     0.60   0  0.416667  0.625
10    0.53   1  0.500000  0.625
11    0.50   1  0.583333  0.625
12    0.41   1  0.666667  0.625
13    0.39   0  0.666667  0.750
14    0.33   1  0.750000  0.750
15    0.30   0  0.750000  0.875
16    0.25   1  0.833333  0.875
17    0.21   1  0.916667  0.875
18    0.18   1  1.000000  0.875
19    0.17   0  1.000000  1.000
"""

print(end='\n')
print('******ROC曲線******')
tp_data = df.loc[:, "真陽性率"].values
fp_data = df.loc[:, "偽陽性率"].values
fp_data = np.append(0, fp_data)
tp_data = np.append(0, tp_data)
print(tp_data)
print(fp_data)
"""
実行結果
[0.         0.08333333 0.08333333 0.16666667 0.16666667 0.25
 0.25       0.25       0.33333333 0.41666667 0.41666667 0.5
 0.58333333 0.66666667 0.66666667 0.75       0.75       0.83333333
 0.91666667 1.         1.        ]
[0.    0.    0.125 0.125 0.25  0.25  0.375 0.5   0.5   0.5   0.625 0.625
 0.625 0.625 0.75  0.75  0.875 0.875 0.875 0.875 1.   ]
"""

fig, ax = plt.subplots()
ax.step(fp_data, tp_data)
ax.set_xlabel('fp rate')
ax.set_ylabel('tp rate')
plt.show()

print(end='\n')
target_data = df.loc[:, "実績"].values
pred_rate = df.loc[:, "予測購入確率"].values
fp_rate, tp_rate, threshold = roc_curve(target_data, pred_rate)
print('真陽性率： ', tp_rate)
print('偽陽性率： ', fp_rate)
"""
実行結果
真陽性率：  [0.         0.08333333 0.08333333 0.16666667 0.16666667 0.25
 0.25       0.41666667 0.41666667 0.66666667 0.66666667 0.75
 0.75       1.         1.        ]
偽陽性率：  [0.    0.    0.125 0.125 0.25  0.25  0.5   0.5   0.625 0.625 0.75  0.75
 0.875 0.875 1.   ]
"""

fig, ax = plt.subplots()
ax.step(fp_rate, tp_rate)
ax.set_xlabel('fp rate')
ax.set_ylabel('tp rate')
plt.show()

print(end='\n')
roc_auc_score(target_data, pred_rate)
print(roc_auc_score(target_data, pred_rate))
"""
実行結果
0.4479166666666667
"""
