# Algorithm 7.1 sin(x)のマクローリン展開による近似

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# マクローリン展開による sin(x) の近似関数（n項まで）
def sin_maclaurin(x, n):
    p = x
    c = p
    for k in range(1,n):
        c = c * (-1)*x**2 / ((2*k + 1) * 2*k)
        p = p + c
    return p

# x の範囲を定義
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
true_sin = np.sin(x_vals)

# 近似の次数をいくつか試す
n_list = [1, 2, 3, 5, 10]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, true_sin, label="True sin(x)", color="black", linewidth=2)

# 各次数で近似結果を描画
for n in n_list:
    approx = [sin_maclaurin(x, n) for x in x_vals]
    plt.plot(x_vals, approx, label=f"{2*n-1} 次の近似")

plt.title("sin(x) のマクローリン展開による近似")
plt.xlabel("x")
plt.ylabel("値")
plt.grid(True)
plt.xlim(-7, 7)         # X軸の範囲を-2π〜 2πを含む範囲で表示
plt.ylim(-2.0, 2.0)     # Y軸の範囲を -2.0〜2.0 に制限
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.show()

