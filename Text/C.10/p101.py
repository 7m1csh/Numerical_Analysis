import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# データ点
x_vals = np.array([1, 2, 3])  # x の値
b_vals = np.array([2, 5, 8])  # y の値

# 方程式の係数行列と定数ベクトル
A = np.column_stack((np.ones_like(x_vals), x_vals))  # 切片と傾きを表す行列
b = b_vals

# 正規方程式 A^T A x = A^T b を解く
AtA = A.T @ A
Atb = A.T @ b
x_ls = np.linalg.solve(AtA, Atb)  # 最小二乗解

# 結果の表示
print("最小二乗解:", x_ls)

# データ点をプロット
plt.scatter(x_vals, b_vals, color='red', label='データ点')

# 最小二乗回帰直線を描画
x_line = np.linspace(0, 4, 100)
y_line = x_ls[0] + x_ls[1] * x_line  # 修正後の回帰直線
plt.plot(x_line, y_line, label='最小二乗回帰直線', color='blue')

# グラフ設定
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title('最小二乗法による回帰直線')
plt.show()

