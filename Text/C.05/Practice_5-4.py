# Condition number

# 条件数の計算
"""
NumPyを使って条件数を求める：
"""

import numpy as np

A = np.array([[4, 2], [2, 3]], dtype=float)
cond_A = np.linalg.cond(A)
print("条件数:", cond_A)

