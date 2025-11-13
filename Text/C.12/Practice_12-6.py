# Practice 12.6 ルンゲ・クッタ法（ロジスティック方程式）
"""
ロジスティック方程式の数値解（RK4）
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 微分方程式（ロジスティック方程式）
r = 0.3
K = 1000
def f(t, x):
    return r * x * (1 - x / K)

# 4次ルンゲ＝クッタ法
def runge_kutta_4(f, t0, x0, h, n_steps):
    t_values = [t0]
    x_values = [x0]
    t = t0
    x = x0
    for _ in range(n_steps):
        k1 = f(t, x)
        k2 = f(t + h/2, x + h/2 * k1)
        k3 = f(t + h/2, x + h/2 * k2)
        k4 = f(t + h,   x + h * k3)
        x = x + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        t_values.append(t)
        x_values.append(x)
    return np.array(t_values), np.array(x_values)

# 実行
t0 = 0
x0 = 10
h = 0.5
n_steps = 100

t_rk4, x_rk4 = runge_kutta_4(f, t0, x0, h, n_steps)

# 解析解との比較
def logistic_analytic(t):
    return K / (1 + ((K - x0)/x0) * np.exp(-r * t))

t_analytic = np.linspace(0, t_rk4[-1], 500)
x_analytic = logistic_analytic(t_analytic)

# グラフ描画
plt.plot(t_rk4, x_rk4, 'o-', label='ルンゲ＝クッタ法（RK4）')
plt.plot(t_analytic, x_analytic, '--', label='解析解')
plt.xlabel('時間 t')
plt.ylabel('個体数 x(t)')
plt.title('ロジスティック方程式の数値解（RK4）')
plt.legend()
plt.grid(True)
plt.show()

