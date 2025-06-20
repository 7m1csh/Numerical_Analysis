# Practice 7.1 ファン・デル・モンド行列
"""
データ点： (1,2),(2,3),(3,5) を通る 2次（最大次数）の補間多項式を、
ファン・デル・モンド行列を使って求め、プロットする。
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 補間点の定義
x_points = np.array([1, 2, 3])
y_points = np.array([2, 3, 5])

# ファン・デル・モンド行列の生成
V = np.vander(x_points, increasing=True)  # 列順を x^0, x^1, ..., x^n にする

# 線形方程式 V @ a = y を解く（多項式係数 a を求める）
coefficients = np.linalg.solve(V, y_points)

# 結果の表示
print("補間多項式の係数（定数項から昇冪）:")
print(coefficients)

# 補間多項式の評価関数
def interpolated_poly(x):
    return sum(c * x**i for i, c in enumerate(coefficients))

# 描画
x_plot = np.linspace(0, 4, 200)
y_plot = interpolated_poly(x_plot)

plt.figure(figsize=(8, 5))
plt.plot(x_plot, y_plot, label='補間多項式', color='blue')
plt.scatter(x_points, y_points, color='red', label='補間点')
plt.title("ファン・デル・モンド行列による多項式補間")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

