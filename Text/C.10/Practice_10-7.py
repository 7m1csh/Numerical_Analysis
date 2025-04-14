# Practice 10.7 Givens回転を用いたQR分解のアニメーション表示

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# スパースな7x7行列
A_original = np.array([
    [4, 0, 0, 0, 0, 0, 0],
    [3, 5, 0, 0, 0, 0, 0],
    [0, 6, 4, 0, 0, 0, 0],
    [0, 0, 2, 3, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 3, 1, 0],
    [0, 0, 0, 0, 0, 2, 6],
], dtype=float)

m, n = A_original.shape
Q = np.eye(m)
R = A_original.copy()
steps = [R.copy()]

# ギブンス回転の適用（途中経過を保存）
for j in range(n):
    for i in range(m-1, j, -1):
        a = R[i-1, j]
        b = R[i, j]
        if np.abs(b) < 1e-10:
            continue
        r = np.hypot(a, b)
        c = a / r
        s = -b / r

        G = np.eye(m)
        G[[i-1, i], [i-1, i]] = c
        G[i-1, i], G[i, i-1] = -s, s

        R = G @ R
        Q = Q @ G.T
        steps.append(R.copy())  # ステップごとのRを保存

# 小さい値を0に
steps = [np.where(np.abs(R_step) < 1e-10, 0, R_step) for R_step in steps]

# アニメーションの作成
fig, ax = plt.subplots(figsize=(5, 5))
matrix_plot = ax.spy(steps[0], precision=1e-10, markersize=10)
ax.set_title("Givens Rotation Step 0")
ax.set_xticks([])
ax.set_yticks([])

def update(frame):
    ax.clear()
    ax.spy(steps[frame], precision=1e-10, markersize=10)
    ax.set_title(f"Givens Rotation Step {frame}")
    ax.set_xticks([])
    ax.set_yticks([])

ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1000, repeat=False)

# plt.close() を削除し、plt.show() を使用
plt.show()

