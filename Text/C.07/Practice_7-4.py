# Practice 7.4 スプライン補間
# 3次スプライン補間（自然条件）の実装例

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 補間点（例：少数のわかりやすい点）
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

# 3次スプライン補間（自然条件：2階微分が端点で0）
cs = CubicSpline(x, y, bc_type='natural')

# 補間結果を描画
x_dense = np.linspace(x[0], x[-1], 300)
y_dense = cs(x_dense)

# グラフ描画
plt.figure(figsize=(8, 5))
plt.plot(x_dense, y_dense, label="3次スプライン補間", color='blue')
plt.scatter(x, y, color='red', label="補間点")
plt.title("3次スプライン補間（自然条件）")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

