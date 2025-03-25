# Practice 9.5 1次元熱伝導方程式の数値解法（陽解法）

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags

# パラメータ設定
N = 10   # 空間分割数
dx = 1.0 / (N - 1)  # 空間刻み
dt = 0.01  # 時間刻み
alpha = 0.1  # 熱拡散係数
lambda_ = alpha * dt / dx**2

# 三重対角行列の構成
main_diag = (1 - 2 * lambda_) * np.ones(N)
off_diag = lambda_ * np.ones(N - 1)

# SciPyのdiagsで三重対角行列を作成
A = diags([off_diag, main_diag, off_diag], [-1, 0, 1]).toarray()

# 初期条件（温度分布）
u = np.zeros(N)
u[N//2] = 1  # 中央に初期温度

# 時間発展
num_steps = 100
for _ in range(num_steps):
    u = A @ u  # 行列 A を適用（時間発展）

# 結果の可視化
plt.plot(np.linspace(0, 1, N), u, marker="o")
plt.xlabel("x")
plt.ylabel("Temperature")
plt.title("Heat Distribution")
plt.show()

