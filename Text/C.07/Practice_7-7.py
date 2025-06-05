#Practice 7.7 パデ近似の可視化

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from scipy.interpolate import pade

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 元の関数
def f(x):
    return np.sqrt((1 + x / 2) / (1 + 2 * x))

# マクローリン展開の係数（手動 or 自動計算）
# f(x) のマクローリン展開の係数を5項（0〜4次）まで手動計算
# 以下は展開済み（近似）：
# f(x) ≈ 1 - 0.75x + 0.625x^2 - 0.703125x^3 + 0.99609375x^4 ...
coeffs = [1, -0.75, 0.625, -0.703125, 0.99609375]

# マクローリン展開関数生成（n次まで）
def taylor_approx(x, order):
    return sum(coeffs[k] * x**k for k in range(order + 1))

# パデ近似（[2/2]）を作成
pade_approx = pade(coeffs, 2)
numerator, denominator = pade_approx

# x の範囲
x = np.linspace(0, 2, 500)
y_true = f(x)

# プロット
plt.figure(figsize=(10, 6))
plt.plot(x, y_true, 'k-', label='元の関数', linewidth=2)

# マクローリン展開（1～4次）
colors = ['r', 'g', 'b', 'm']
for n in range(1, 5):
    y_taylor = taylor_approx(x, n)
    plt.plot(x, y_taylor, linestyle='--', color=colors[n-1], label=f'マクローリン展開 {n}次')

# パデ近似
y_pade = numerator(x) / denominator(x)
plt.plot(x, y_pade, 'c-.', linewidth=2, label='パデ近似 [2/2]')

# 装飾
plt.title(r'$f(x) = \sqrt{(1 + \frac{x}{2}) / (1 + 2x)}$ の近似')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
#plt.ylim(0, 1.2)
plt.ylim(-1, 2)
plt.show()

