# 演習問題 4.6
"""
行列 A = [[1, 1, 0], [0, 1, 1], [0, 1, 0]] の
列ベクトルに対して、グラム・シュミット直交化を適用せよ。
※プログラムでは、行と列が入れ替わっていることに注意
"""

import numpy as np

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

# 動作テスト
A = np.array([
    [1, 0, 0],
    [1, 1, 1],
    [0, 1, 0]
])

Q = gram_schmidt(A)

print("正規直交ベクトル（行ごと）:")
np.set_printoptions(precision=4, suppress=True)  # 出力を見やすく
print(Q)

