# 演習問題 4.6.1
"""
演習問題4.6.1 を図示化。
直交化前と直交化後を別々に表示。
---
行列 A = [[1, 1, 0], [0, 1, 1], [0, 1, 0]] の
列ベクトルに対して、グラム・シュミット直交化を適用せよ。
※プログラムでは、行と列が入れ替わっていることに注意
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gram_schmidt(A):
    """
    グラム・シュミットの直交化法を用いて、正規直交ベクトルを求める
    :param A: 入力ベクトル（各行が1つのベクトル）(m × n 行列, m: ベクトル数, n: 次元)
    :return: 正規直交ベクトルの集合 (m × n 行列)
    """
    A = np.array(A, dtype=np.float64)  # 入力行列を NumPy 配列に変換
    m, n = A.shape  # m: ベクトル数, n: 次元数
    U = np.zeros((m, n))  # 直交化されたベクトル
    Q = np.zeros((m, n))  # 正規直交ベクトル（最終出力）

    for i in range(m):
        # Step 1: 直交化 (Orthogonalization)
        u_i = A[i].copy()
        for j in range(i):
            u_i -= np.dot(Q[j], A[i]) * Q[j]

        U[i] = u_i  # 直交化されたベクトルを保存

        # Step 2: 正規化 (Normalization)
        norm = np.linalg.norm(U[i])
        if norm > 1e-10:  # ゼロに近いベクトルは無視（線形従属の可能性）
            Q[i] = U[i] / norm  # ノルムで割って単位ベクトルにする
        else:
            Q[i] = 0  # ゼロベクトルを設定（線形従属の可能性）

    return Q

# ベクトルを図示する関数
def plot_vectors(vectors, colors, title):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('equal') # アスペクト比を1:1:1に設定

    for i, vector in enumerate(vectors):
        x, y, z = vector
        ax.quiver(0, 0, 0, x, y, z, color=colors[i], length=1.0, arrow_length_ratio=0.1)

    # 軸ラベル
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 軸の範囲を調整
    max_val = np.max(np.abs(vectors))
    ax.set_xlim([-max_val - 0.5, max_val + 0.5])
    ax.set_ylim([-max_val - 0.5, max_val + 0.5])
    ax.set_zlim([-max_val - 0.5, max_val + 0.5])

    ax.set_title(title)
    plt.show()

# 動作テスト
A_orig = np.array([
    [1, 0, 0],
    [1, 1, 1],
    [0, 1, 0]
])

print(f"テスト用の行列：\n{A_orig}\n")

Q = gram_schmidt(A_orig)

print("正規直交ベクトル（行ごと）:")
np.set_printoptions(precision=4, suppress=True)  # 出力を見やすく
print(Q)


# 行列 A の列ベクトルを抽出して転置
A_vectors = A_orig.T
Q_vectors = Q.T

# ベクトルの色
colors_A = ['r', 'g', 'b']
colors_Q = ['m', 'y', 'c']

# ベクトル A の図示
plot_vectors(A_vectors, colors_A, 'Original Vectors (Columns of A)')

# ベクトル Q の図示
plot_vectors(Q_vectors, colors_Q, 'Orthonormal Vectors (Columns of Q)')
