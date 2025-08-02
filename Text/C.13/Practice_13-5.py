# Practice 13.5 1次元非定常熱伝導方程式の数値解（陽解法）
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
nx = 6                  # 空間分割数（0～5の6点）
nt = 100                # 時間ステップ数
alpha = 1.0             # 拡散係数
dx = 1.0                # 空間ステップ（無次元なので1.0）
dt = 0.1                # 時間ステップ
r = alpha * dt / dx**2  # 安定性パラメータ（FTCS法のためr<=0.5が安定）

# 初期化
theta = np.ones(nx) * 20.0    # 初期温度
theta[0] = 0.0                # 左端境界条件
theta[-1] = 20.0              # 右端境界条件

# 時間発展を保存
theta_hist = [theta.copy()]

# FTCSスキームで時間発展
for _ in range(nt):
    theta_new = theta.copy()
    for i in range(1, nx-1):
        theta_new[i] = theta[i] + r * (theta[i+1] - 2*theta[i] + theta[i-1])
    theta_new[0] = 0.0       # 境界条件再設定
    theta_new[-1] = 20.0
    theta = theta_new
    theta_hist.append(theta.copy())

# 可視化
theta_hist = np.array(theta_hist)
X = np.arange(nx)
T = np.arange(nt+1) * dt

plt.figure(figsize=(8, 6))
for i in range(0, nt+1, 10):
    plt.plot(X, theta_hist[i], label=f'τ={T[i]:.1f}')
plt.xlabel('X')
plt.ylabel('θ')
plt.title('非定常熱伝導方程式の時間発展　：　陽的差分法（FTCSスキーム）')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

