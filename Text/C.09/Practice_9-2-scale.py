# Plactice 9.2 固有値と固有ベクトルの図示

import numpy as np
import matplotlib.pyplot as plt

# 行列 A
A = np.array([[2, 1],
              [1, 2]])

# 固有値と固有ベクトルを求める
eigenvalues, eigenvectors = np.linalg.eig(A)

# 固有ベクトル
v1 = eigenvectors[:, 0]  # λ1 = 3 に対応する固有ベクトル
v2 = eigenvectors[:, 1]  # λ2 = 1 に対応する固有ベクトル

# 変換後のベクトル
Av1 = A @ v1
Av2 = A @ v2

# 図の設定
fig, ax = plt.subplots(figsize=(6, 6))
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xticks(range(-2, 3))
ax.set_yticks(range(-2, 3))
ax.grid(True, linestyle='--', alpha=0.6)

# 固有ベクトルとその変換後のベクトルを描画
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label="v1 (λ=3)")
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label="v2 (λ=1)")
ax.quiver(0, 0, Av1[0], Av1[1], angles='xy', scale_units='xy', scale=1, color='r', alpha=0.5, label="A*v1")
ax.quiver(0, 0, Av2[0], Av2[1], angles='xy', scale_units='xy', scale=1, color='b', alpha=0.5, label="A*v2")

# 凡例を右下に移動
ax.legend(loc="lower right")

# タイトル
ax.set_title("Eigenvectors and transformed vectors")

# 表示
plt.show()

