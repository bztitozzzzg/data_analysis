import numpy as np

a = np.array([[0,1,10],[0,1,10]])
print(a, end='\n\n')
b = a.copy()
print(b, end='\n\n')
#a2 = a.reshape(3,2)
a2 = a.copy()
print(a2, end='\n\n')
print(b * a2)
"""
実行結果
ValueError: operands could not be broadcast together with shapes (2,3) (3,2)
行と列が異なる 2つの 2D 配列を追加できないこと
→同じ形状の配列同士でないと、NG
"""