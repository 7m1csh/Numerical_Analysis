# Practice 9.13 特異値の一つが 0 に近い場合の特異値分解の視覚化アニメーション

print(
"""
特異値の一つが 0 に近い場合の特異値分解の視覚化アニメーション
特異値分解は、行列を回転、拡大縮小、反転の3つの操作に分解する方法です。
特異値 ≈ 0.01 と非常に小さいため、楕円がほぼ線に潰れます。
特異値分解において、特異値が 0 に近づくほど「変形が片方向にのみ作用」し、情報の次元が失われます（ランクが落ちる）
"""
)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 単位円の生成
theta = np.linspace(0, 2*np.pi, 100)
circle = np.array([np.cos(theta), np.sin(theta)])  # 2xN

# 特異値の1つが 0 に近い行列
A_near_rank_def = np.array([
    [1, 0],
    [0, 0.01],
    [1, 0]
], dtype=float)

print(f"特異値の1つが 0 に近い行列 A :\n{A_near_rank_def}")

# SVD
U2, S2, VT2 = np.linalg.svd(A_near_rank_def)
Sigma2 = np.zeros_like(A_near_rank_def)
np.fill_diagonal(Sigma2, S2)

# 各ステップでの変換
circle_VT2 = VT2 @ circle
circle_S2 = Sigma2[:2, :2] @ circle_VT2
circle_U2 = U2[:2, :2] @ circle_S2  # 修正箇所

# アニメーション設定
fig2, ax2 = plt.subplots(figsize=(5, 5))
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.set_aspect('equal')
line2, = ax2.plot([], [], 'b')
title2 = ax2.set_title("")

# 初期化
def init2():
    line2.set_data([], [])
    title2.set_text("")
    return line2, title2

# フレーム更新
def animate2(i):
    if i < 20:
        t = i / 20
        intermediate = circle + t * (circle_VT2 - circle)
        label = "Step 1: Apply V^T"
    elif i < 40:
        t = (i - 20) / 20
        intermediate = circle_VT2 + t * (circle_S2 - circle_VT2)
        label = "Step 2: Apply Σ (one ~ 0)"
    else:
        t = (i - 40) / 20
        intermediate = circle_S2 + t * (circle_U2 - circle_S2)
        label = "Step 3: Apply U"
    
    line2.set_data(intermediate[0], intermediate[1])
    title2.set_text(label)
    return line2, title2

ani2 = animation.FuncAnimation(fig2, animate2, init_func=init2,
                               frames=60, interval=100, blit=True)
plt.show()

