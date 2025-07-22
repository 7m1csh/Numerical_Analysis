# Practice 13.3 2次元定常熱伝導方程式（ラプラス方程式）

import numpy as np
import matplotlib.pyplot as plt

# パラメータ
nx, ny = 50, 50
max_iter = 1000
tolerance = 1e-4

# 格子点の初期化
u = np.zeros((nx+1, ny+1))

# Dirichlet境界条件の設定（例：上端を1、他を0）
u[:, -1] = 1.0  # y = 1 の温度を1に固定（上辺）

# ヤコビ法による反復
for k in range(max_iter):
    u_new = u.copy()
    for i in range(1, nx):
        for j in range(1, ny):
            u_new[i, j] = 0.25 * (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1])

    # 収束判定（最大変化量）
    diff = np.max(np.abs(u_new - u))
    u = u_new
    if k % 100 == 0:
        print(f"iteration {k}: max difference = {diff:.5e}")
    if diff < tolerance:
        print(f"Converged at iteration {k}")
        break

# 結果の表示
plt.imshow(u.T, origin='lower', cmap='hot', extent=[0,1,0,1])
plt.colorbar(label='Temperature')
plt.title('2D Laplace Equation (Steady-State Heat)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

