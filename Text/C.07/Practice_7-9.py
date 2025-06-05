# Practice 7.9 f(x)=sqrt((1+x/2)/(1+2x))のパデ近似をハンケル行列で求める

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom
from scipy.linalg import hankel

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 対象関数
def f(x):
    return np.sqrt((1 + x/2) / (1 + 2*x))

# マクローリン展開係数（数値的に計算: 中心差分）
def taylor_coefficients(f, order, h=1e-5):
    coeffs = []
    for n in range(order + 1):
        # n階微分の中心差分近似（実用上十分）
        deriv = sum([(-1)**k * binom(n, k) * f((n/2 - k)*h) for k in range(n + 1)]) / h**n
        coeffs.append(deriv / np.math.factorial(n))
    return np.array(coeffs)

# パデ近似の分母係数（ハンケル行列使用）
def pade_denominator_hankel(a, n):
    #H = hankel(a[n:2*n], a[2*n-1:2*n+n-1])
    #b = -a[2*n:2*n+n]
    H = hankel(a[n:2*n], a[n:2*n])  # 修正: 最後の行のスライシングを調整
    b = -a[n+1:2*n+1]  # 修正: b のスライシングを調整
    q = np.linalg.solve(H, b)
    q = np.concatenate(([1.0], q))
    return q

# パデ近似の分子係数
def pade_numerator(a, q, m):
    N = m + len(q) - 1
    f_series = np.array([a[k] if k < len(a) else 0 for k in range(N+1)])
    q_padded = np.array([q[k] if k < len(q) else 0 for k in range(N+1)])
    p = np.convolve(f_series, q_padded)[:m+1]
    return p

# マクローリン展開の次数
order = 8
a = taylor_coefficients(f, order)

# パデ近似（[4/4]）
m = n = 4
q = pade_denominator_hankel(a, n)
p = pade_numerator(a, q, m)

# パデ近似関数
def pade_approx(x):
    num = np.polyval(p[::-1], x)
    den = np.polyval(q[::-1], x)
    return num / den

# 各種近似をプロット
x = np.linspace(0, 2, 400)
y_true = f(x)
y_taylor1 = sum(a[k] * x**k for k in range(1 + 1))
y_taylor2 = sum(a[k] * x**k for k in range(2 + 1))
y_taylor3 = sum(a[k] * x**k for k in range(3 + 1))
y_taylor4 = sum(a[k] * x**k for k in range(4 + 1))
y_pade = pade_approx(x)

# プロット
plt.figure(figsize=(10, 6))
plt.plot(x, y_true, 'k-', label='f(x) = sqrt((1 + x/2)/(1 + 2x))')
plt.plot(x, y_taylor1, 'g--', label='マクローリン展開（1次）')
plt.plot(x, y_taylor2, 'b--', label='マクローリン展開（2次）')
plt.plot(x, y_taylor3, 'c--', label='マクローリン展開（3次）')
plt.plot(x, y_taylor4, 'm--', label='マクローリン展開（4次）')
plt.plot(x, y_pade, 'r-.', label='パデ近似 [4/4]')
plt.title('関数 f(x) の近似: マクローリン展開 vs パデ近似')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(0, 3)
plt.grid(True)
plt.legend()
plt.show()

