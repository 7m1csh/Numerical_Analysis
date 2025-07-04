# Practice 12.7 ルンゲ＝クッタ法の可視化

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 可視化に都合の良い関数（例：f(t, y) = y - t^2 + 1）
def f(t, y):
    return y - t**2 + 1

# 初期条件とステップ幅
t0 = 0
y0 = 0.5
h = 0.5

# ルンゲ＝クッタ法（1ステップのみ）
k1 = f(t0, y0)
k2 = f(t0 + h/2, y0 + h/2 * k1)
k3 = f(t0 + h/2, y0 + h/2 * k2)
k4 = f(t0 + h, y0 + h * k3)
y1 = y0 + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

# 関数の本体を描画する準備
T = np.linspace(t0, t0 + h, 100)
Y_true = lambda t: (t + 1)**2 - 0.5 * np.exp(t)  # この微分方程式の解析解（参考）
Y_func = f

# 描画
fig, ax = plt.subplots(figsize=(10, 6))

# 実際の関数の形（fのグラフではなく、y(t)の概形として参考に）
tt = np.linspace(t0, t0 + h, 100)
yt = (tt + 1)**2 - 0.5 * np.exp(tt)
ax.plot(tt, yt, label='参考：解析解の曲線', color='lightgray', linestyle='--')

# 接線（傾き）のベクトルを表示
def draw_slope(t, y, k, label, color):
    dt = 0.1
    dy = k * dt
    ax.arrow(t, y, dt, dy, head_width=0.02, head_length=0.05, fc=color, ec=color, label=label)

# 各 k の接線（傾き）を描画
draw_slope(t0, y0, k1, 'k1', 'red')
draw_slope(t0 + h/2, y0 + h/2 * k1, k2, 'k2', 'orange')
draw_slope(t0 + h/2, y0 + h/2 * k2, k3, 'k3', 'green')
draw_slope(t0 + h, y0 + h * k3, k4, 'k4', 'blue')

# 点の描画
ax.plot(t0, y0, 'ko', label='開始点 (t0, y0)')
ax.plot(t0 + h, y1, 'ko', label='予測点 (t0+h, y1)', markerfacecolor='none', markersize=10)

# 注釈
ax.text(t0, y0 + 0.2, '$(t_0, y_0)$', fontsize=12)
ax.text(t0 + h, y1 + 0.2, '$(t_0+h, y_1)$', fontsize=12)

ax.set_xlabel('t')
ax.set_ylabel('y')

# タイトルに微分方程式と初期条件を記述
ax.set_title("ルンゲ＝クッタ法（RK4）の可視化\n$y' = y - t^2 + 1$ を $y(0) = 0.5$ で解く", fontsize=14)

ax.legend()
ax.grid(True)

plt.show()

