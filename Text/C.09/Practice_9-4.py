# Practice 9.4 トーマス法による連立一次方程式の解法

import numpy as np
from scipy.linalg import solve_banded

# 三重対角行列のバンド行列表現
A_banded = np.array([
    [0, -1, -1, -1],  # 上対角成分
    [2,  2,  2,  2],  # 主対角成分
    [-1, -1, -1, 0]   # 下対角成分
])
print("三重対角行列のバンド行列表現: \n", A_banded, "\n")

# 右辺ベクトル
b = np.array([1, 0, 0, 1])
print("右辺ベクトル:\n", b, "\n")

# トーマス法で解く
x = solve_banded((1, 1), A_banded, b)
print("トーマス法で説いた結果:", x)

