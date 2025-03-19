# Algorithm 5.1 ガウスの消去法（軸選択なし）の Python 実装

# Gaussian elimination without pivoting

import numpy as np

def gauss_elim(A, b):
    n = len(b)
    for k in range(n-1):
        if A[k, k] == 0 :
            raise ValueError("ゼロ割りが発生します。軸選択を導入してください。")

        for i in range(k+1, n):
                m = A[i, k] / A[k, k]
                for j in range(k, n):
                    A[i, j] = A[i, j] - m * A[k, j]
                b[i] = b[i] - m * b[k]
    return A, b

# Example
A = np.array([[1, 2, 3], [1, 3, 3], [2, 5, 7]], dtype=float)
b = np.array([1, 2, 2], dtype=float)
A, b = gauss_elim(A, b)
print("Updated matrix A:")
print(A)
print("Updated vector b:")
print(b)
