# Practice 10.6 ギブンス回転によるQR分解

import numpy as np

# スパースな7x7行列
A = np.array([
    [4, 0, 0, 0, 0, 0, 0],
    [3, 5, 0, 0, 0, 0, 0],
    [0, 6, 4, 0, 0, 0, 0],
    [0, 0, 2, 3, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 3, 1, 0],
    [0, 0, 0, 0, 0, 2, 6],
], dtype=float)

m, n = A.shape
Q = np.eye(m)
R = A.copy()

# ギブンス回転の適用（下三角の非ゼロ成分を順番に消去）
for j in range(n):
    for i in range(m-1, j, -1):
        a = R[i-1, j]
        b = R[i, j]
        if np.abs(b) < 1e-10:
            continue
        r = np.hypot(a, b)
        c = a / r
        s = -b / r

        # ギブンス回転行列の適用（Rの行を直接更新）
        G = np.eye(m)
        G[[i-1, i], [i-1, i]] = c
        G[i-1, i], G[i, i-1] = -s, s

        R = G @ R
        Q = Q @ G.T  # QはGの転置をかける

# 小さい値は0に
Q[np.abs(Q) < 1e-10] = 0
R[np.abs(R) < 1e-10] = 0

np.set_printoptions(precision=4, suppress=True)
print("QR分解対称のスパース行列 A :\n", A)
print("Q :\n", Q)
print("\nR :\n", R)
print("\nA ≈ Q @ R :\n", Q @ R)

