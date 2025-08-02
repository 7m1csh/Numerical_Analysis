# Practice 13.6 1次元非定常熱伝導方程式の数値解（クランク・ニコルソン法）
"""
$\frac{\partial \theta}{\partial \tau} = \frac{\partial^2 \theta}{\partial X^2}$
$\theta$ : 無次元温度
$\tau$ : 無次元時間
X : 無次元座標

について、以下の条件で可視化する。

[座標Xの変化]
i=0,1,2,3,4,5

[初期条件]
$\tau$=0, $\theta$[i]=20

[境界条件]
$\tau > 0$, $\theta$[0]=0, $\theta$[5]=20
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# パラメータ設定
N = 6           # 格子点数
dx = 1.0        # 空間刻み
dt = 0.1        # 時間刻み
alpha = 1.0     # 拡散係数 (無次元では1.0)
r = alpha * dt / (dx ** 2)

# 初期条件
theta = np.full(N, 20.0)
theta[0] = 0.0
theta[-1] = 20.0

# 保存用
history = [theta.copy()]
time_steps = 20  # 総時間ステップ数

# クランク・ニコルソンの係数行列を作成
A = np.zeros((N - 2, N - 2))
B = np.zeros((N - 2, N - 2))

for i in range(N - 2):
    A[i, i] = 1 + r
    B[i, i] = 1 - r
    if i > 0:
        A[i, i - 1] = -r / 2
        B[i, i - 1] = r / 2
    if i < N - 3:
        A[i, i + 1] = -r / 2
        B[i, i + 1] = r / 2

# 時間発展
for t in range(time_steps):
    b = B @ theta[1:-1]
    # 境界条件の影響を考慮
    b[0] += (r / 2) * (theta[0] + theta[0])
    b[-1] += (r / 2) * (theta[-1] + theta[-1])

    # 線形方程式を解く
    theta_new_inner = np.linalg.solve(A, b)
    theta[1:-1] = theta_new_inner

    history.append(theta.copy())

# 可視化
X = np.arange(N)
T = np.arange(time_steps + 1) * dt

plt.figure(figsize=(10, 6))
for i, state in enumerate(history[::2]):  # 2ステップごと表示
    plt.plot(X, state, label=f"τ={i*2*dt:.1f}")

plt.xlabel("X（無次元座標）")
plt.ylabel("θ（無次元温度）")
plt.title("クランク・ニコルソン法による熱伝導のシミュレーション")
plt.grid(True)
plt.legend()
plt.show()

