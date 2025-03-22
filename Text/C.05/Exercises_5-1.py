# 演習問題 5.1
"""
以下の連立方程式のグラフをoctaveを用いて図式化する.
各方程式で１枚のグラフになるようにして、線ごとに色分けする。
(1)  [[2, 1], [-1, 2]] * [x, y]^t = [5, 0]^t
(2)  [[2, 1], [4, 2]] * [x, y]t = [5, 0]^t
(3)  [[2, 1], [-1, 2], [1, 3]] * [x, y]^t = [5, 0, 2]^t

(3)式おいて、右辺ベクトルを b=[5, 0, α]^t としたとき、
この方程式が解を持つαを求めグラフを描く。
α = 5
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_system(A, b, title):
    """2元連立方程式 Ax = b をグラフ化"""
    x = np.linspace(-10, 10, 400)  # x の範囲
    colors = ['r', 'b', 'g']  # 3本までの線を色分け
    labels = []

    plt.figure(figsize=(6, 6))

    for i in range(A.shape[0]):  # 各方程式ごとに直線を描画
        if A[i, 1] != 0:  # y の係数が 0 でない場合
            y = (b[i] - A[i, 0] * x) / A[i, 1]
            plt.plot(x, y, colors[i % len(colors)], label=f"{A[i,0]}x + {A[i,1]}y = {b[i]}")
        else:  # y の係数が 0 の場合（垂直線）
            x_vert = np.full_like(x, b[i] / A[i, 0])
            plt.plot(x_vert, x, colors[i % len(colors)], label=f"{A[i,0]}x = {b[i]}")

    plt.axhline(0, color='gray', linewidth=0.5)  # x軸
    plt.axvline(0, color='gray', linewidth=0.5)  # y軸
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.title(title)
    plt.show()

# (1) 一意解を持つ
A1 = np.array([[2, 1], [-1, 2]])
b1 = np.array([5, 0])
plot_system(A1, b1, "System (1)")

# (2) 平行な直線（解なし）
A2 = np.array([[2, 1], [4, 2]])
b2 = np.array([5, 0])
plot_system(A2, b2, "System (2)")

# (3) 3本の直線（オーバーコンストレインド）
A3 = np.array([[2, 1], [-1, 2], [1, 3]])
b3 = np.array([5, 0, 2])
plot_system(A3, b3, "System (3)")

# α = 5 の場合のグラフ
A3 = np.array([[2, 1], [-1, 2], [1, 3]])
b3 = np.array([5, 0, 5])
plot_system(A3, b3, "System (3) with α = 5")

