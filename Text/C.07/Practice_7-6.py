# Practice 7.6 パデ近似
"""
関数 f(x) = exp(x) を題材に、パデ近似を実装し、
テイラー展開と比較可視化
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.special import factorial

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

def true_func(x):
    return np.exp(x)

def taylor_exp(x, order=6):
    return sum((x**k) / factorial(k) for k in range(order + 1))

x = np.linspace(-6, 6, 500)
y_true = true_func(x)
y_taylor = taylor_exp(x)

# テイラー展開係数（0次〜6次）
taylor_coeffs = [1/factorial(k) for k in range(7)]
pade_approx = interpolate.pade(taylor_coeffs, 3)
numerator, denominator = pade_approx
y_pade = numerator(x) / denominator(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_true, 'k-', label='正確な e^x', linewidth=2)
plt.plot(x, y_taylor, 'b--', label='テイラー展開 (6次)', linewidth=1.5)
plt.plot(x, y_pade, 'r-.', label='パデ近似 [3/3]', linewidth=1.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("e^x のテイラー展開とパデ近似の比較（広範囲）")
plt.legend()
plt.ylim(-20, 100)
plt.show()

