# 演習問題 10.1.2
"""
ベクトルa1,a2,b は「演習問題10.1.1のとおり
a1 = [1, 1, 1]^t
a2 = [-1, 0, 1]^t
b  = [-1, 11/10, 3]^t

A = [a1, a2] としたとき、
A^t@A を係数行列とする連立1次方程式 A^t@A@x=b を解いて、
1次式による最小2乗近似を求める。
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# ベクトル定義
a1 = np.array([1, 1, 1])
a2 = np.array([-1, 0, 1])
b  = np.array([-1, 11/10, 3])

# 行列 A を列ベクトルとして構成（3×2 行列）
A = np.column_stack((a1, a2))
print("行列 A:")
print(A)

# 行列 A の転置
A_T = A.T
print("\n行列 A の転置 A^T:")
print(A_T)

# 正規方程式 (A^T A)x = A^T b の構築と解法
AtA = A.T @ A
Atb = A.T @ b
x = np.linalg.solve(AtA, Atb)
print("\n連立方程式の係数行列:")
print(AtA)
print("\n連立方程式の右辺:")
print(Atb)
print()

# 結果表示
print("最小二乗解 x:")
print(x)

# 近似ベクトル A @ x の表示
b_approx = A @ x
print("\nA @ x による近似ベクトル:")
print(b_approx)

# 元の b との誤差
residual = b - b_approx
print("\n残差ベクトル (b - A @ x):")
print(residual)
print("\n残差ノルム（2乗誤差の平方根）:")
print(np.linalg.norm(residual))

