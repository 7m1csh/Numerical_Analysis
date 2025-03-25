# Practice 9.6 三重対角行列の連立一次方程式をTDMA法で解く

import numpy as np
from scipy.sparse import diags

def tdma_solver(a, b, c, d):
    n = len(d)

    # 前進消去
    for i in range(1, n):
        w = a[i-1] / b[i-1]
        b[i] = b[i] - w * c[i-1]
        d[i] = d[i] - w * d[i-1]

    # 後退代入
    x = np.zeros(n)
    x[-1] = d[-1] / b[-1]
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - c[i] * x[i+1]) / b[i]

    return x

# 三重対角行列の成分
a = np.array([1, 1, 1], dtype=float)     # a_2, a_3, a_4
b = np.array([4, 4, 4, 4], dtype=float)  # b_1, b_2, b_3, b_4
c = np.array([1, 1, 1], dtype=float)     # c_1, c_2, c_3
d = np.array([5, 5, 5, 5], dtype=float)  # 右辺ベクトル
T = diags([a, b, c], offsets=[-1, 0, 1]).toarray()
print("三重対角行列 T:\n", T, "\n")
print("右辺ベクトル  :\n", d, "\n")

# TDMA法で解く
x_tdma = tdma_solver(a.copy(), b.copy(), c.copy(), d.copy())
print("TDMA法による解             :", x_tdma)

# numpy.linalg.solve で検算
A = np.array([[4, 1, 0, 0],
              [1, 4, 1, 0],
              [0, 1, 4, 1],
              [0, 0, 1, 4]])

x_numpy = np.linalg.solve(A, d)
print("numpy.linalg.solve による解:", x_numpy)

