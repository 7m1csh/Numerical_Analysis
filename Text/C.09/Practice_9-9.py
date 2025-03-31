# ゲルシュゴリン円盤を可視化

import numpy as np
import matplotlib.pyplot as plt

# 行列 A の定義
A = np.array([[4, -1, 2],
              [1, 3, -2],
              [0, -1, 5]])

n = A.shape[0]

# ゲルシュゴリン円盤の計算
centers = np.diag(A)  # 対角成分（円の中心）
radii = np.sum(np.abs(A), axis=1) - np.abs(centers)  # 半径

# プロットの設定
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(min(centers) - max(radii) - 1, max(centers) + max(radii) + 1)
ax.set_ylim(-max(radii) - 1, max(radii) + 1)

# x, y 軸の描画
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# 各ゲルシュゴリン円盤を描画
for i in range(n):
    circle = plt.Circle((centers[i], 0), radii[i], color='b', alpha=0.3, edgecolor='black')
    ax.add_patch(circle)
    ax.plot(centers[i], 0, 'ro')  # 円の中心を赤い点で表示

# ラベルとタイトル
ax.set_title("Gershgorin Circles")
ax.set_xlabel("Real Part")
ax.set_ylabel("Imaginary Part")
ax.grid(True, linestyle="--", alpha=0.5)

# 表示
print(f"ゲルシュゴリン円盤を可視化する行列：\n{A}\n")
print(f"行列 A の固有値：{np.linalg.eigvals(A)}")
plt.show()

