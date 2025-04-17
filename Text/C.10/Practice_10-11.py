# Practice 10.11 主成分分析
"""
身長と体重の関係について主成分分析を行う。
身長: 165 158 153 174 171 157 177 163 164 172
体重:  67  56  48  68  62  49  79  56  58  70
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# データの定義（身長, 体重）
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

# Step 1: データの中心化（平均を引く）
mean = np.mean(data, axis=0)
centered_data = data - mean

# Step 2: 特異値分解
U, S, VT = np.linalg.svd(centered_data, full_matrices=False)

# 主成分（方向）は VT の行
principal_components = VT

# Step 3: 散布図と主成分を描画
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(centered_data[:, 0], centered_data[:, 1], label='データ点')
ax.axhline(0, color='gray', lw=1)
ax.axvline(0, color='gray', lw=1)

# 主成分を矢印で描画（スケーリングあり）
for i in range(2):
    vec = principal_components[i] * S[i]  # 特異値でスケーリング
    ax.arrow(0, 0, vec[0], vec[1],
             color=f"C{i+1}", width=0.5, head_width=1.5, length_includes_head=True,
             label=f"主成分 {i+1}")

ax.set_title("中心化された身長・体重の散布図と主成分")
ax.set_xlabel("身長（中心化）")
ax.set_ylabel("体重（中心化）")
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

