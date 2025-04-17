# Practice 10.12 回帰分析
"""
身長と体重の関係について回帰分析を行う。
身長: 165 158 153 174 171 157 177 163 164 172
体重:  67  56  48  68  62  49  79  56  58  70
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# 身長と体重のデータ
heights = np.array([165,158,153,174,171,157,177,163,164,172])
weights = np.array([67,56,48,68,62,49,79,56,58,70])

# 回帰分析（最小二乗法）
A = np.vstack([heights, np.ones_like(heights)]).T
coef, residuals, _, _ = np.linalg.lstsq(A, weights, rcond=None)

slope, intercept = coef
print(f"回帰直線: 体重 = {slope:.2f} * 身長 + {intercept:.2f}")

# 回帰直線のプロット
x_vals = np.linspace(min(heights), max(heights), 100)
y_vals = slope * x_vals + intercept

plt.figure(figsize=(8,6))
plt.scatter(heights, weights, color='blue', label='データ点')
plt.plot(x_vals, y_vals, color='red', label='回帰直線')
plt.xlabel('身長 (cm)')
plt.ylabel('体重 (kg)')
plt.title('回帰分析：身長 → 体重')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()

