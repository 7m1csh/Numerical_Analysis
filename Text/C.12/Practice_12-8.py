# Practice 12.8 陽解法と陰解法

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 微分方程式: y' = -2y + 2 - e^{-4t}
def f(t, y):
    return -2 * y + 2 - np.exp(-4 * t)

# 厳密解（比較用）
def exact_solution(t):
    return 1 + 0.5 * np.exp(-4 * t) - 0.5 * np.exp(-2 * t)

# 初期条件と時間ステップ
y0 = 1
t0 = 0
h = 0.2
n_steps = 10

t_values = [t0]
y_explicit = [y0]
y_implicit = [y0]

# 陽解法（オイラー法）
y = y0
t = t0
for i in range(n_steps):
    y = y + h * f(t, y)
    t = t + h
    t_values.append(t)
    y_explicit.append(y)

# 陰解法（後退オイラー法）:
# y_{n+1} = y_n + h * f(t_{n+1}, y_{n+1}) を解く必要がある
# ここでは単純な解法（1次の陰関数を解く）を使う
y = y0
t = t0
t_values_imp = [t0]
for i in range(n_steps):
    t_next = t + h
    # 陰関数: y_{n+1} = y_n + h*(-2*y_{n+1} + 2 - e^{-4*t_{n+1}})
    # => y_{n+1}(1 + 2h) = y_n + h*(2 - e^{-4*t_{n+1}})
    rhs = y + h * (2 - np.exp(-4 * t_next))
    y = rhs / (1 + 2 * h)
    t = t_next
    t_values_imp.append(t)
    y_implicit.append(y)

# 厳密解
t_dense = np.linspace(0, 2, 100)
y_exact = exact_solution(t_dense)

# プロット
plt.figure(figsize=(10, 6))
plt.plot(t_dense, y_exact, 'k--', label='厳密解', linewidth=2)
plt.plot(t_values, y_explicit, 'o-', label='陽解法（オイラー）', color='blue')
plt.plot(t_values_imp, y_implicit, 's-', label='陰解法（後退オイラー）', color='red')
plt.title("陽解法 vs 陰解法 の比較\n$y' = -2y + 2 - e^{-4t},\ y(0) = 1$")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

