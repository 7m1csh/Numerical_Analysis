# Practice 13.1 1次元熱伝導方程式の有限差分法（陽解法）
#
#\[ \frac {\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2} \]
"""
u(x,t)：位置xにおける時刻tの温度
α> 0：熱拡散係数（熱伝導率）

u[int(nx/2)] = 1.0：初期温度分布として、中央を加熱。
境界条件：端点 x=0, x=L は温度固定（Dirichlet条件）
安定性：  r ≤0.5 でないと発散
"""
import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
L = 1.0            # 棒の長さ
T = 0.1            # 総時間
alpha = 1.0        # 熱拡散係数

nx = 50            # 空間分割数
dx = L / nx
#dt = 0.0002        # 時間刻み
dt = 0.0001        # 時間刻み
nt = int(T / dt)   # 時間ステップ数

r = alpha * dt / dx**2
print(f"r = {r:.3f}  (r <= 0.5 で安定)")

# 初期条件
u = np.zeros(nx + 1)
u[int(nx / 2)] = 1.0  # 真ん中を加熱

# 結果保存用
results = [u.copy()]

# 時間発展
for n in range(nt):
    u_new = u.copy()
    for i in range(1, nx):
        u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1])
    u = u_new
    if n % (nt // 5) == 0:
        results.append(u.copy())

# 可視化
x = np.linspace(0, L, nx + 1)
for i, u_snap in enumerate(results):
    plt.plot(x, u_snap, label=f"t = {i * T/5:.3f}")
plt.xlabel("x")
plt.ylabel("Temperature")
plt.legend()
plt.title("1D Heat Equation (Explicit Method)")
plt.grid(True)
plt.show()

