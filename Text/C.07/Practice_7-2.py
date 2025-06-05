# Practice 7.2 ラグランジュ補間
# 3点補間 (0, 1), (0.5, -1), (1, 1)

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 補間点
#x_points = np.array([1, 2, 3])
#y_points = np.array([2, 3, 5])
x_points = np.array([0, 0.5, 1])
y_points = np.array([1, -1, 1])

# ラグランジュ基底関数の定義
def L(j, x):
    xj = x_points[j]
    terms = [(x - x_points[m]) / (xj - x_points[m]) for m in range(len(x_points)) if m != j]
    return np.prod(terms, axis=0)

# 補間多項式 P(x) の定義
def lagrange_poly(x):
    return sum(y_points[j] * L(j, x) for j in range(len(x_points)))

# グラフ表示
x_vals = np.linspace(0, 4, 200)
y_vals = lagrange_poly(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="ラグランジュ補間多項式", color="blue")
plt.scatter(x_points, y_points, color="red", label="補間点")
plt.title("ラグランジュ補間")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.ylim(-2, 6)
plt.show()

