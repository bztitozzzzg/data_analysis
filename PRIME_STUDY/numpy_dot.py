import numpy as np
a = np.array([1, 3])
b = np.array([-1, 5])
c = np.array([[1, 2], [3, 4]])
d = a @ b
e = np.dot(c, a)
print(d, e)

"""
実行結果
14 [ 7 15]
"""
