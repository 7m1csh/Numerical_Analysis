# Residual

# 残差の計算
"""
NumPyを使って残差を求める：
"""

import numpy as np

A = np.array([[4, 2], [2, 3]], dtype=float)
b = np.array([4, 5], dtype=float)

# Ax = b を解く
x = np.linalg.solve(A, b)

# 残差を計算
r = b - np.dot(A, x)

print(f"係数行列 A ：\n {A}\n")
print(f"右辺ベクトル b ：\n {b}\n")
print(f"解ベクトル x ：\n {x}\n")

print("残差:", r)
print("残差ノルム:", np.linalg.norm(r))

