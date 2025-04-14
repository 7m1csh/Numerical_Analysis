# Practice 10-3 グラムシュミッドの直交化法による QR 分解

import numpy as np

# 与えられた行列 A
A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)

# グラム・シュミットの直交化法による QR 分解
m, n = A.shape
Q = np.zeros((m, n))
R = np.zeros((n, n))

for j in range(n):
    v = A[:, j]
    for i in range(j):
        R[i, j] = np.dot(Q[:, i], A[:, j])
        v = v - R[i, j] * Q[:, i]
    R[j, j] = np.linalg.norm(v)
    Q[:, j] = v / R[j, j]

# 小さい値を 0 にする
Q[np.abs(Q) < 1e-10] = 0
R[np.abs(R) < 1e-10] = 0

# 結果の表示（固定小数点表示）
np.set_printoptions(precision=6, suppress=True)
print("グラムシュミッドの直交化法による QR 分解\n")
print("行列 A:")
print(A)
print("\n直交行列 Q:")
print(Q)
print("\n上三角行列 R:")
print(R)

# QR 分解の確認 (A ≈ QR)
A_reconstructed = Q @ R
print("\nA (再構成):")
print(A_reconstructed)

