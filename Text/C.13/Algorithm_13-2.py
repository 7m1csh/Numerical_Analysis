# Algorithm 13.3 2次元ラプラス方程式の反復解法（逐次加算緩和法）
"""
input:  境界条件 $u_{00},...,u_{m+1,m+1}$ , 初期状態 $u_{11},...,u_{mm}$
        加速緩和係数 omega
output: ラプラス方程式を満たす u
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# パラメータ
omega = 1.5
m = 50
max_iter = 10000
tolerance = 1e-4
h = 1 / (m + 1)

# 格子点の初期化
u = np.zeros((m+1, m+1))
r = u.copy()

# Dirichlet境界条件の設定（例：上端を1、他を0）
u[:,  0] = 0.0  # y = 0 の温度を0に固定（下辺）
u[:, -1] = 1.0  # y = 1 の温度を1に固定（上辺）
u[0,  :] = 0.0  # x = 0 の温度を0に固定（左辺）
u[-1, :] = 0.0  # x = 1 の温度を0に固定（右辺）

# SOR法による反復
for k in range(max_iter):
    for i in range(1, m):
        for j in range(1, m):
            r[i, j] = (1 / h**2 ) * (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - 4 * u[i, j])
            u[i, j] = u[i, j] + omega * (h**2 / 4) * r[i, j]

    # 収束判定（最大変化量）
    diff = np.max(np.abs(r[1:-1, 1:-1]))
    if k % 100 == 0:
        print(f"iteration {k}: max difference = {diff:.5e}")
    if diff < tolerance:
        print(f"Converged at iteration {k}")
        break

# 結果の表示
plt.imshow(u.T, origin='lower', cmap='hot', extent=[0,1,0,1])
plt.colorbar(label='Temperature')
plt.title(f'２次元ラプラス方程式の反復解法（SOR法）ω={omega}')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

