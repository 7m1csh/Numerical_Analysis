# Practice 12.5 オイラー法（ロジスティック方程式）
"""
ロジスティック方程式のオイラー法による近似
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# パラメータ（ロジスティック方程式）
r = 0.3
K = 1000
def f(t, u):
    return r * u * (1 - u / K)

# オイラー法の実装
def euler(f, t0, u0, h, n_steps):
    t_values = [t0]
    u_values = [u0]
    t = t0
    u = u0
    for _ in range(n_steps):
        u = u + h * f(t, u)
        t = t + h
        t_values.append(t)
        u_values.append(u)
    return np.array(t_values), np.array(u_values)

# 実行
t0 = 0
u0 = 10
h = 0.5
n_steps = 100

t, u = euler(f, t0, u0, h, n_steps)

# 解析解（比較用）
def logistic_analytic(t):
    return K / (1 + ((K - u0)/u0) * np.exp(-r * t))

t_analytic = np.linspace(0, t[-1], 500)
u_analytic = logistic_analytic(t_analytic)

# 描画
plt.plot(t, u, 'o-', label='オイラー法による近似')
plt.plot(t_analytic, u_analytic, '--', label='解析解')
plt.xlabel('時間 t')
plt.ylabel('個体数 u(t)')
plt.title('ロジスティック方程式のオイラー法による近似')
plt.legend()
plt.grid(True)
plt.show()

