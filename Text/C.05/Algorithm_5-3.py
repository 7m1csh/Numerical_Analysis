# Algorithm 5.3 前進後退代入

# forward substitution and backward substitution

import numpy as np

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

# 例：LU分解の結果を用いた連立方程式の解法
L = np.array([[1, 0, 0], [2, 1, 0], [3, 2, 1]], dtype=float)
U = np.array([[2, 1, 3], [0, 1, -5], [0, 0, 5]], dtype=float)
b = np.array([5, 6, 9], dtype=float)

# Step 1: 前進代入で Ly = b を解く
y = forward_substitution(L, b)
print("y =", y)

# Step 2: 後退代入で Ux = y を解く
x = backward_substitution(U, y)
print("x =", x)

