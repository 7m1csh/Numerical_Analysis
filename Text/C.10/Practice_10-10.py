# Practice 10.10 ラグランジュの未定乗数法の視覚化
"""
目的関数: f(x, y) = 2x + 3y
制約条件: g(x, y) = x^2 + y^2 - 1 = 0 (単位円)
ラグランジュの未定乗数法を用いて、制約条件の下での最大値と最小値を求める
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# 制約条件: x^2 + y^2 = 1 (単位円)
theta = np.linspace(0, 2*np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# 目的関数: f(x, y) = 2x + 3y
# 等高線をいくつか描画するための準備
x_range = np.linspace(-1.5, 1.5, 100)
y_range = np.linspace(-1.5, 1.5, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = 2*X + 3*Y

# ラグランジュの未定乗数法による最大値の候補
# ∇f = λ∇g
# (2, 3) = λ(2x, 2y)
# 2 = 2λx  => x = 1/λ
# 3 = 2λy  => y = 3/(2λ)
# 制約条件に代入: (1/λ)^2 + (3/(2λ))^2 = 1
# 1/λ^2 + 9/(4λ^2) = 1
# (4 + 9) / (4λ^2) = 1
# 13 / (4λ^2) = 1
# λ^2 = 13/4
# λ = ±√(13)/2

# λ = √(13)/2 のとき
lambda_pos = np.sqrt(13) / 2
x_max = 1 / lambda_pos
y_max = 3 / (2 * lambda_pos)
f_max = 2 * x_max + 3 * y_max

# λ = -√(13)/2 のとき (参考: 最小値)
lambda_neg = -np.sqrt(13) / 2
x_min = 1 / lambda_neg
y_min = 3 / (2 * lambda_neg)
f_min = 2 * x_min + 3 * y_min

# グラフ描画
plt.figure(figsize=(8, 8))
plt.plot(x_circle, y_circle, label='$x^2 + y^2 = 1$ (制約条件)')
contour = plt.contour(X, Y, Z, levels=np.linspace(f_min - 1, f_max + 1, 10), cmap='viridis', linestyles='dashed', alpha=0.7, label='等高線 $f(x, y) = 2x + 3y$')
plt.clabel(contour, inline=True, fontsize=8)
plt.plot(x_max, y_max, 'ro', markersize=8, label='最大値 ($x \approx {:.2f}, y \approx {:.2f}, f \approx {:.2f}$)'.format(x_max, y_max, f_max))
plt.plot(x_min, y_min, 'bo', markersize=8, label='最小値 ($x \approx {:.2f}, y \approx {:.2f}, f \approx {:.2f}$)'.format(x_min, y_min, f_min))
plt.xlabel('x')
plt.ylabel('y')
plt.title('ラグランジュの未定乗数法の例題の視覚化')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box') # グラフを正方形にする

# グラフの左下にタイトルを追加
plt.text(
    x=0.02,  # x座標（グラフの左下に配置するため小さい値を指定）
    y=0.05,  # y座標（グラフの左下に配置するため小さい値を指定）
    s="目的関数: f(x, y) = 2x + 3y",  # 表示するテキスト
    fontsize=10,  # フォントサイズ
    ha='left',  # 水平方向の配置
    va='bottom',  # 垂直方向の配置
    transform=plt.gca().transAxes  # グラフ座標系に基づいて配置
)

# グラフを表示
plt.show()

