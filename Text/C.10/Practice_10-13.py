# Practice 10.13 主成分分析と回帰分析の比較
"""
身長と体重の関係について主成分分析と回帰分析の比較を行う。
身長: 165 158 153 174 171 157 177 163 164 172
体重:  67  56  48  68  62  49  79  56  58  70

🔴 回帰直線（赤）：
体重（目的変数）を身長（説明変数）で予測するための「最小二乗直線」。
誤差の最小化方向は縦方向（体重の差）。

🟢 第1主成分（緑）：
データ全体のばらつき方向を示すベクトル。
誤差の最小化方向は垂直方向（最短距離）。

実際の違いの意味
回帰分析は「予測」に向いている。
主成分分析（PCA）は「次元削減・可視化・特徴抽出」に使われる。
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# 元のデータ
data = np.array([
    [165, 67],
    [158, 56],
    [153, 48],
    [174, 68],
    [171, 62],
    [157, 49],
    [177, 79],
    [163, 56],
    [164, 58],
    [172, 70]
], dtype=float)

heights = data[:, 0]
weights = data[:, 1]

# 中心化（主成分用）
mean = np.mean(data, axis=0)
centered_data = data - mean

# 特異値分解（PCA用）
U, S, VT = np.linalg.svd(centered_data, full_matrices=False)
principal_vector = VT[0] * S[0]  # 第1主成分（スケーリング込み）

# 回帰分析（最小二乗法）
A = np.vstack([heights, np.ones_like(heights)]).T
coef, _, _, _ = np.linalg.lstsq(A, weights, rcond=None)
slope, intercept = coef

# グラフ描画
fig, ax = plt.subplots(figsize=(8, 7))

# 散布図
ax.scatter(centered_data[:, 0], centered_data[:, 1], label='データ点（中心化）', color='blue')

# 主成分（矢印）
ax.arrow(0, 0, principal_vector[0], principal_vector[1],
         color='green', width=0.5, head_width=1.5, length_includes_head=True, label='第1主成分')

# 回帰直線（中心化に対応）
x_vals = np.linspace(min(heights), max(heights), 100)
x_centered = x_vals - mean[0]
y_centered = (slope * x_vals + intercept) - mean[1]
ax.plot(x_centered, y_centered, color='red', label='回帰直線')

# その他設定
ax.axhline(0, color='gray', lw=1)
ax.axvline(0, color='gray', lw=1)
ax.set_xlabel('身長（中心化）')
ax.set_ylabel('体重（中心化）')
ax.set_title('主成分と回帰直線の比較')
ax.grid(True)
ax.legend()
ax.set_aspect('equal')
plt.tight_layout()
plt.show()

