import numpy as np
a = np.full((1, 5), np.e).T.ravel()
b = np.linspace(0, 1, 5)
c = np.hstack([a, b])
print(a[-1], c[-1])

"""
実行結果
2.718281828459045 1.0
"""
