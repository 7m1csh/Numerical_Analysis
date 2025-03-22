# 演習問題 5.2
"""
以下の連立方程式をガウスの消去法を用いて解を求めよ。
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * [x1, x2, x3]^t = [1, 2, 2]^t
"""
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

        # Step 2: 後退代入で Ax = y を解く
        x = backward_substitution(A, b)
    return A, b, x

def backward_substitution(U, y):
    """後退代入: U * x = y を解く"""
    n = len(y)
    x = np.zeros(n, dtype=float)

    for i in range(n-1, -1, -1):  # 逆順に計算
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x


# ガウスの消去法で連立方程式を解く
A = np.array([[1, 2, 3], [1, 3, 3], [2, 5, 7]], dtype=float)
b = np.array([1, 2, 2], dtype=float)
A, b, x = gauss_elim(A, b)

print("Updated matrix A:")
print(A)
print("")

print("Updated vector b:")
print(b)
print("")

print("Solution vector x:")
print(x)
