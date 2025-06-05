# Practice 7.8 exp(x)のパデ近似をハンケル行列で求める

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import hankel

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 対象関数：f(x) = e^x のテイラー展開係数（マクローリン展開）
# f(x) = 1 + x + x^2/2! + x^3/3! + ...
def taylor_coefficients_exp(N):
    return np.array([1 / np.math.factorial(k) for k in range(N)])

# パデ近似の分母係数を求める（m=n=3の場合）
def pade_denominator_hankel(a, n):
    """
    与えられたテイラー係数列 a に対して、
    パデ近似 [n/n] の分母係数をハンケル行列を使って求める
    """
    H = hankel(a[n:2*n], a[2*n-1:2*n+n-1])  # ハンケル行列 H_{i,j} = a_{i+j+n}
    b = -a[2*n:2*n+n]
    q = np.linalg.solve(H, b)
    q = np.concatenate(([1.0], q))  # 定数項は 1 とする
    return q

# パデ近似の分子係数を求める
def pade_numerator(a, q, m):
    """
    分子係数を求める。a: テイラー係数, q: 分母係数, m: 分子次数
    """
    # P(x) = Q(x) * f(x) を x^m 以下で切る
    N = m + len(q) - 1
    f_series = np.array([a[k] if k < len(a) else 0 for k in range(N+1)])
    q_padded = np.array([q[k] if k < len(q) else 0 for k in range(N+1)])
    p = np.convolve(f_series, q_padded)[:m+1]
    return p

# テイラー展開係数を取得
N = 10
a = taylor_coefficients_exp(N)

# パデ近似の係数（[3/3] 近似）
m = n = 3
q = pade_denominator_hankel(a, n)
p = pade_numerator(a, q, m)

# パデ近似関数を定義
def pade_approx(x):
    num = np.polyval(p[::-1], x)   # 分子
    den = np.polyval(q[::-1], x)   # 分母
    return num / den

# 元の関数と近似を描画
x = np.linspace(-2, 2, 400)
y_true = np.exp(x)
y_pade = pade_approx(x)
y_taylor = sum(a[k] * x**k for k in range(2*n+1))

# プロット
plt.figure(figsize=(10, 6))
plt.plot(x, y_true, 'k-', label='正確な $e^x$')
plt.plot(x, y_taylor, 'b--', label='テイラー展開 (6次)')
plt.plot(x, y_pade, 'r-.', label='パデ近似 [3/3]')
plt.title('テイラー展開とパデ近似の比較（ハンケル行列使用）')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(0, 4)
plt.grid(True)
plt.legend()
plt.show()

