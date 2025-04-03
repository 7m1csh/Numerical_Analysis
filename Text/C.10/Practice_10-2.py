import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # または 'IPAexGothic' など

# 与えられた方程式の係数行列と定数ベクトル
A = np.array([[1, 1], [2, 1], [3, 1]])
b = np.array([2, 5, 8])

# 擬似逆行列を用いた最小二乗解
x_ls = np.linalg.pinv(A) @ b  # Moore-Penrose 逆行列を使用

# 結果の表示
print("最小二乗解:", x_ls)

# データ点をプロット
x_vals = np.array([1, 2, 3])  # xの値
b_vals = np.array([2, 5, 8])  # yの値
plt.scatter(x_vals, b_vals, color='red', label='データ点')

# 最小二乗回帰直線を描画
x_line = np.linspace(0, 4, 100)
y_line = x_ls[0] * x_line + x_ls[1]
plt.plot(x_line, y_line, label='最小二乗回帰直線', color='blue')

# グラフ設定
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title('擬似逆行列を用いた最小二乗法による回帰直線')
plt.show()

