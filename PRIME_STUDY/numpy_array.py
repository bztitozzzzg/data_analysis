import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2, 3])
print(a[-1:, [1, 2]], b.dtype)

"""
実行結果
[[5 6]] int32
"""
