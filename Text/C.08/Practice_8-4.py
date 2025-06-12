# Practice 8.4 割線法の可視化

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 関数と初期値
f = lambda x: x**2 - 2
x_vals = [1.0, 2.0]
max_iter = 6

# 割線法の近似値リスト
approximations = x_vals.copy()
for _ in range(max_iter - 2):
    x0, x1 = approximations[-2], approximations[-1]
    if abs(f(x1) - f(x0)) < 1e-14:
        break
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    approximations.append(x2)

# グラフの準備
x = np.linspace(0, 2.2, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label='f(x)')
ax.axhline(0, color='black', lw=1)
line, = ax.plot([], [], 'r-', label='Secant line')
dot1, = ax.plot([], [], 'bo')  # 1つ前の点
dot2, = ax.plot([], [], 'go')  # 現在の点
intersection, = ax.plot([], [], 'ro')  # x軸との交点
vline = Line2D([], [], color='green', linestyle='--')  # 垂線
ax.add_line(vline)
text = ax.text(0.05, 0.1, '', transform=ax.transAxes)  # テキスト位置調整

ax.set_title('割線法による反復の可視化')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.set_ylim(-2, 2)

# 更新関数
def update(i):
    if i >= len(approximations) - 1:
        return line, dot1, dot2, intersection, vline, text

    x0 = approximations[i]
    x1 = approximations[i + 1]
    y0 = f(x0)
    y1 = f(x1)

    # 割線
    slope = (y1 - y0) / (x1 - x0)
    intercept = y1 - slope * x1
    x_line = np.array([x0, x1])
    y_line = slope * x_line + intercept
    line.set_data(x_line, y_line)

    # 点と交点
    x_int = -intercept / slope
    dot1.set_data(x0, y0)
    dot2.set_data(x1, y1)
    intersection.set_data(x_int, 0)

    # 垂線（x_int から f(x_int) へ）
    y_func = f(x_int)
    vline.set_data([x_int, x_int], [0, y_func])

    text_str = f'反復: {i + 1}'
    if i == len(approximations) - 2:
        text_str += '（完了）'
    text.set_text(text_str)

    return line, dot1, dot2, intersection, vline, text

# アニメーション設定
#ani = FuncAnimation(fig, update, frames=len(approximations)-1, interval=1200, repeat=False)
ani = FuncAnimation(fig, update, frames=len(approximations)-1, interval=3000, repeat=False)

plt.show()

