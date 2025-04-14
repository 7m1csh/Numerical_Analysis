# ギブンス回転を用いたQR分解

import numpy as np

def givens_rotation(A):
    """ ギブンス回転を用いたQR分解 """
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()

    for j in range(n):
        for i in range(m-1, j, -1):  # 上から順にゼロにする
            a, b = R[i-1, j], R[i, j]
            r = np.hypot(a, b)  # sqrt(a^2 + b^2) の計算
            if r < 1e-10:  # すでに 0 ならスキップ
                continue
            c, s = a / r, -b / r

            G = np.eye(m)
            G[[i-1, i], [i-1, i]] = c
            G[i-1, i], G[i, i-1] = -s, s

            R = G @ R  # 左から回転行列を掛ける
            Q = Q @ G.T  # Q を更新

    return Q, R

# 例: 行列 A
A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)

# ギブンス回転による QR 分解
Q, R = givens_rotation(A)

# 小さい値を 0 にする
Q[np.abs(Q) < 1e-10] = 0
R[np.abs(R) < 1e-10] = 0

# 結果の表示（固定小数点表示）
np.set_printoptions(precision=6, suppress=True)
print("ギブンス回転による QR 分解\n")
print("行列 A:")
print(A)
print("\nQ (直交行列):")
print(Q)
print("\nR (上三角行列):")
print(R)

# QR 分解の確認 (A ≈ QR)
A_reconstructed = Q @ R
print("\nA (再構成):")
print(A_reconstructed)

