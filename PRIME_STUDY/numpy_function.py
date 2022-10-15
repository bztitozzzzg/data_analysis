import numpy as np
a = np.array([0, 9, 99, 999])
a = a + 1
a = a * 100
b = np.log10(a)
print(a[1], b[2])

"""
実行結果
1000 4.0
"""
