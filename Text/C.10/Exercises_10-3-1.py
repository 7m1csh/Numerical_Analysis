# 演習問題 10.3  の論理で特異値分解を用いて行列 A の特異値分解を求め単位円を変換する様子をプロット

import numpy as np
import matplotlib.pyplot as plt

# Aの定義
a1 = np.array([1, 1, 1])
a2 = np.array([-1, 0, 1])
A = np.column_stack((a1, a2))  # 3x2 行列

# AtA の固有値分解
AtA = A.T @ A
eigvals, V = np.linalg.eigh(AtA)
singular_values = np.sqrt(np.maximum(eigvals, 0))  # 特異値

# 左特異ベクトル U の計算
U = np.zeros((A.shape[0], A.shape[1]))
for i in range(A.shape[1]):
    if singular_values[i] > 1e-10:
        U[:, i] = A @ V[:, i] / singular_values[i]

Sigma = np.diag(singular_values)

# 単位円の生成（2次元）
theta = np.linspace(0, 2 * np.pi, 100)
circle = np.array([np.cos(theta), np.sin(theta)])  # 2x100

# 単位円を V^T → Σ → U の順に変換（幾何的意味を示す）
ellipse1 = V @ circle          # V^T による回転（右特異ベクトル）
ellipse2 = Sigma @ ellipse1    # Σ によるスケーリング（特異値）
ellipse3 = U @ ellipse2        # U による回転（左特異ベクトル）

# プロット
fig = plt.figure(figsize=(12, 4))

# V^T 変換
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(circle[0], circle[1], label='unit circle')
ax1.plot(ellipse1[0], ellipse1[1], label='after V^T')
ax1.set_title('Step 1: V^T (rotation)')
ax1.axis('equal')
ax1.legend()
ax1.grid(True)

# Σ 変換
ax2 = fig.add_subplot(1, 3, 2)
ax2.plot(ellipse1[0], ellipse1[1], label='after V^T')
ax2.plot(ellipse2[0], ellipse2[1], label='after Σ')
ax2.set_title('Step 2: Σ (scaling)')
ax2.axis('equal')
ax2.legend()
ax2.grid(True)

# U 変換
ax3 = fig.add_subplot(1, 3, 3)
ax3.plot(ellipse2[0], ellipse2[1], label='after Σ')
ax3.plot(ellipse3[0], ellipse3[1], label='final: A @ x')
ax3.set_title('Step 3: U (rotation)')
ax3.axis('equal')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.show()

