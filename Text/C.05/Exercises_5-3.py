# 演習問題 5.3
"""
以下の連立方程式(演習問題5.2)行列Aとベクトルx,bで表し、LU分解を用いて解を求めよ。
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * [x, y, z]^t = [1, 2, 2]^t
"""

# LU decomposition without pivoting

import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.eye(n)  # 単位行列 (対角成分が1)
    U = A.astype(float).copy()  # Aのコピーを作成

    for k in range(n - 1):
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]  # 乗数を計算
            U[i, k:] -= m * U[k, k:]  # Uの該当行を更新
            L[i, k] = m  # Lに記録

    return L, U

def forward_substitution(L, b):
    """前進代入: L * y = b を解く"""
    n = len(b)
    y = np.zeros(n, dtype=float)

    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])  # Σの部分計算
    return y

def backward_substitution(U, y):
    """後退代入: U * x = y を解く"""
    n = len(y)
    x = np.zeros(n, dtype=float)

    for i in range(n-1, -1, -1):  # 逆順に計算
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x


# LU分解を用いて連立方程式を解く
A = np.array([[1, 2, 3], [1, 3, 3], [2, 5, 7]], dtype=float)
b = np.array([1, 2, 2], dtype=float)
L, U = lu_decomposition(A)

y = forward_substitution(L, b)
x = backward_substitution(U, y)

print("Matrix A:")
print(A)
print("")

print("Vector b:")
print(b)
print("")

print("L:")
print(L)
print("")

print("U:")
print(U)
print("")

print("Solution vector x:")
print(x)
print("")

