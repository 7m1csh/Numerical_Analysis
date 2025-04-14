# Practice 10-4 ハウスホルダー変換による QR 分解

import numpy as np

# 与えられた行列 A
A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)

# ハウスホルダー変換による QR 分解
def householder_qr(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()
    
    for i in range(n):
        x = R[i:, i]
        e1 = np.zeros_like(x)
        e1[0] = np.linalg.norm(x)
        v = x - e1
        v = v / np.linalg.norm(v) if np.linalg.norm(v) > 1e-10 else v
        
        H = np.eye(m)
        H[i:, i:] -= 2.0 * np.outer(v, v)
        R = H @ R
        Q = Q @ H.T
    
    return Q, R

Q, R = householder_qr(A)

# 小さい値を 0 にする
Q[np.abs(Q) < 1e-10] = 0
R[np.abs(R) < 1e-10] = 0

# 結果の表示（固定小数点表示）
np.set_printoptions(precision=6, suppress=True)
print("ハウスホルダー変換による QR 分解\n")
print("行列 A:")
print(A)
print("\nQ:")
print(Q)
print("\nR:")
print(R)

# QR 分解の確認 (A ≈ QR)
A_reconstructed = Q @ R
print("\nA (再構成):")
print(A_reconstructed)

