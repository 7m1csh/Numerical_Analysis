# Practice 10.8 特異値分解とアニメーション
"""
特異値分解を用いて行列の変換を視覚化するアニメーションを作成
特異値分解は、行列を3つの行列の積に分解する。
具体的には、行列 A を次のように分解：
A = UΣV^T
"""

print(
"""
行列 A は、「空間を回転・伸縮・再回転」する操作を表す：
A = 回転1(V^T) →  スケーリング(Σ) →  回転2(U)
"""
)

import numpy as np

# 例の行列 A（3x2行列）
A = np.array([
    [1, 0],
    [0, 2],
    [1, 0]
], dtype=float)

# 特異値分解
U, S, VT = np.linalg.svd(A)

# 特異値を対角行列に変換（S はベクトルなので）
Sigma = np.zeros_like(A, dtype=float)
np.fill_diagonal(Sigma, S)

# 小さい値を0にする（見やすくするた列め）
U_fixed = np.where(np.abs(U) < 1e-10, 0, U)
Sigma_fixed = np.where(np.abs(Sigma) < 1e-10, 0, Sigma)
VT_fixed = np.where(np.abs(VT) < 1e-10, 0, VT)

print(f"例題の行列 A :\n{A}\n\n")
print(f"特異値分解結果\n\n")
print(f"直交行列(出力空間の基底ベクトル) :\n {U_fixed}\n\n")
print(f"特異値行列 Σ : {Sigma_fixed}\n\n")
print(f"転置直交行列(入力空間の基底ベクトル) :\n {VT_fixed}\n\n")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 入力ベクトル空間の単位ベクトル（Vの列ベクトル）
v1 = VT.T[:, 0]  # 最初の列（本来のVの1列目）
v2 = VT.T[:, 1]  # 2列目

# 単位円上の点を生成
theta = np.linspace(0, 2*np.pi, 100)
circle = np.array([np.cos(theta), np.sin(theta)])  # 2xN

# 各変換ステップの出力を計算
circle_VT = VT @ circle        # Step 1: V^T
circle_S = Sigma[:2, :2] @ circle_VT  # Step 2: Σ

# circle_S を (3, 100) に拡張
circle_S_padded = np.vstack([circle_S, np.zeros((1, circle_S.shape[1]) )])

circle_U = U[:, :2] @ circle_S        # Step 3: U

# アニメーション設定
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
line, = ax.plot([], [], 'r')
title = ax.set_title("")

# 初期化
def init():
    line.set_data([], [])
    title.set_text("")
    return line, title

# 各フレーム更新
def animate(i):
    if i < 20:
        # Step 1: V^T
        t = i / 20
        intermediate = circle + t * (circle_VT - circle)
        label = "Step 1: Apply V^T"
    elif i < 40:
        # Step 2: Σ
        t = (i - 20) / 20
        intermediate = circle_VT + t * (circle_S - circle_VT)
        label = "Step 2: Apply Σ (Scaling)"
    else:
        # Step 3: U
        t = (i - 40) / 20
        intermediate = circle_S_padded + t * (circle_U - circle_S_padded)
        label = "Step 3: Apply U"
    
    line.set_data(intermediate[0], intermediate[1])
    title.set_text(label)
    return line, title

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=60, interval=100, blit=True)

print(
"""
アニメーションの流れ
Step 1： V^Tを適用
単位円が「回転」または「反転」される。
これは入力空間の基底を変更する操作である。

Step 2： Σを適用
円が楕円にスケーリングされる（特異値による変形）
特異値が 0 に近いほど、潰れていく。

Step 3： U を適用
楕円が再び回転（または反転）される。
最終的に、これが A による変換の結果になる。
"""
)

plt.show()  # アニメーションを表示

