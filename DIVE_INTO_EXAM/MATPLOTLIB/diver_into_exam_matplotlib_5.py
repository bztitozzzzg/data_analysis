from traceback import print_tb
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

science_score = [43, 78, 73, 86, 89, 61, 84, 66, 87, 89]
math_score = [51, 71, 69, 82, 80, 60, 88, 56, 85, 99]

fig, ax = plt.subplots()
ax.scatter(science_score, math_score)
plt.show()
"""
実行結果

"""

print(end='\n')

fig, ax = plt.subplots()
ax.scatter(science_score, math_score, marker='v')
plt.show()

print(end='\n')


df = pd.DataFrame([["A", 43, 51, 81, 61, 65],
                   ["B", 78, 71, 83, 88, 86],
                   ["C", 73, 69, 89, 51, 69],
                   ["D", 86, 82, 87, 85, 62],
                   ["E", 89, 80, 77, 55, 63],
                   ["F", 61, 60, 86, 90, 90],
                   ["G", 84, 88, 65, 74, 84],
                   ["H", 66, 56, 98, 84, 72],
                   ["I", 87, 85, 56, 58, 51],
                   ["J", 89, 99, 88, 58, 66]],
                  columns=["生徒", "理科", "数学", "国語", "英語", "社会"]
                  )
df
print(df)
"""
実行結果
  生徒  理科  数学  国語  英語  社会
0  A  43  51  81  61  65
1  B  78  71  83  88  86
2  C  73  69  89  51  69
3  D  86  82  87  85  62
4  E  89  80  77  55  63
5  F  61  60  86  90  90
6  G  84  88  65  74  84
7  H  66  56  98  84  72
8  I  87  85  56  58  51
9  J  89  99  88  58  66
"""

print(end='\n')

pd.plotting.scatter_matrix(df)
plt.show()

print(end='\n')

_ = scatter_matrix(df)
