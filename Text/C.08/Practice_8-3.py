# Practice 8.3 ニュートン法の視覚化

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'


# 関数と導関数（例：√2 を求める）
def f(x):
    return x**2 - 2

def df(x):
    return 2*x
"""
# 関数と導関数（例: cos(x) - 1 ）
def f(x):
    return np.cos(x) - x

def df(x):
    return -np.sin(x) - 1
"""
# ニュートン法のステップ保存
x0 = 1.0
iterations = 6
x_vals = [x0]

for _ in range(iterations):
    x_next = x_vals[-1] - f(x_vals[-1]) / df(x_vals[-1])
    x_vals.append(x_next)

# 描画範囲
x_plot = np.linspace(0.5, 2.0, 400)
y_plot = f(x_plot)

# アニメーション準備
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_plot, y_plot, label=r'$f(x) = x^2 - 2$', color='blue')
ax.axhline(0, color='gray', linewidth=1)
point, = ax.plot([], [], 'ro')  # 現在の点
tangent_line, = ax.plot([], [], 'r--')  # 接線
vertical_line, = ax.plot([], [], 'g:')  # 垂線
#text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
text = ax.text(0.05, 0.8, '', transform=ax.transAxes)

ax.set_ylim(-2, 2)
ax.set_xlim(0.5, 2.0)
ax.grid(True)
ax.legend()

def init():
    point.set_data([], [])
    tangent_line.set_data([], [])
    vertical_line.set_data([], [])
    text.set_text('')
    return point, tangent_line, vertical_line, text

def animate(i):
    x_n = x_vals[i]
    fx = f(x_n)
    dfx = df(x_n)

    # 接線の傾きと切片
    slope = dfx
    intercept = fx - slope * x_n

    # 接線の描画
    x_tan = np.linspace(x_n - 0.5, x_n + 0.5, 10)
    y_tan = slope * x_tan + intercept
    tangent_line.set_data(x_tan, y_tan)

    # 点
    point.set_data([x_n], [fx])

    # 次の近似解 x_{n+1}
    x_next = x_vals[i+1]
    y_next = f(x_next)

    # 垂線（緑色）：x = x_next の縦線
    vertical_line.set_data([x_next, x_next], [0, y_next])

    # テキスト更新
    if i == len(x_vals) - 2:
        text.set_text(f'反復 {i}: x = {x_n:.6f}（完了）')
        text.set_color('green')  # 色を変える
    else:
        text.set_text(f'反復 {i}: x = {x_n:.6f}')
        text.set_color('black')
    return point, tangent_line, vertical_line, text

ani = FuncAnimation(fig, animate, frames=len(x_vals)-1,
                    init_func=init, blit=True, interval=4000, repeat=False)

plt.title("ニュートン法の視覚化（接線と垂線）")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

