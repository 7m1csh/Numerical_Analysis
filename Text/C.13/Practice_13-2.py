# Practice 13.2 2次元の陽的差分法

import numpy as np
import matplotlib.pyplot as plt

# パラメータ
Lx, Ly = 1.0, 1.0        # 領域の大きさ
nx, ny = 50, 50          # 空間分割数
dx = Lx / nx
dy = Ly / ny
alpha = 1.0              # 熱拡散係数

dt = 0.0002
#T = 0.01                # 総時間
T = 0.1                 # 総時間
nt = int(T / dt)

r = alpha * dt / dx**2   # dx=dyと仮定
print(f"r = {r:.3f}  (r <= 0.25 で安定)")

# 初期条件：中央を局所加熱
u = np.zeros((nx+1, ny+1))
u[nx//2, ny//2] = 1.0

# 時間発展
for n in range(nt):
    u_new = u.copy()
    for i in range(1, nx):
        for j in range(1, ny):
            u_new[i, j] = u[i, j] + r * (
                u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - 4 * u[i, j]
            )
    u = u_new.copy()
    if n % (nt // 5) == 0:
    #if n % 50 == 0:     #更新頻度を増やす。
        plt.clf()
        plt.imshow(u.T, origin='lower', cmap='hot', extent=[0, Lx, 0, Ly])
        plt.colorbar(label='Temperature')
        plt.title(f"Time = {n * dt:.4f}")
        #plt.pause(0.1)
        plt.pause(1.0)  #数値を大きくすると、各スナップの表示時間が長くなる。

plt.show()

