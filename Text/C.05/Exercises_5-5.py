# 演習問題 5.5
"""
以下の連立方程式(演習問題5.2)行列Aとベクトルx,bで表し、
選択軸付きLU分解を用いて解を求めよ。
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * [x, y, z]^t = [1, 2, 2]^t
"""

# LU decomposition without pivoting

import numpy as np

def lu_decomposition(A):
   n = len(A)
   L = np.eye(n)  # 単位行列 (対角成分が1)
   U = A.astype(float).copy()  # Aのコピーを作成

   for k in range(n - 1):
       # 軸選択（部分ピボット選択）
       max_row = np.argmax(np.abs(U[k:n, k])) + k
       if U[max_row, k] == 0:
           raise ValueError("行列は特異行列であり、解が一意に定まりません。")

       # 行の入れ替え
       if max_row != k:
           print(f"Swap row {k+1} <---> {max_row+1}\n")
           U[[k, max_row]] = U[[max_row, k]]
           b[k], b[max_row] = b[max_row], b[k]
           AP = U.copy()

       for i in range(k + 1, n):
           m = U[i, k] / U[k, k]  # 乗数を計算
           U[i, k:] -= m * U[k, k:]  # Uの該当行を更新
           L[i, k] = m  # Lに記録

   return L, U, AP

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
L, U, AP = lu_decomposition(A)

y = forward_substitution(L, b)
x = backward_substitution(U, y)

print(f"Matrix A:\n{A}")
print(" |")
print(" V")
print(f"{AP}\n")
print(f"Vector b:\n{b}\n")
print(f"L:\n{L}\n")
print(f"U:\n{U}\n")
print(f"Solution vector x:\n{x}")

