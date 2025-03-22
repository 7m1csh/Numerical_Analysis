# 演習問題 5.4
"""
以下の連立方程式(演習問題5.2)行列Aとベクトルx,bで表し、LU分解を用いて解を求めよ。
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * x1 = [1, 0, 0]^t
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * x2 = [0, 1, 0]^t
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * x3 = [0, 0, 1]^t
 
X = [x1, x2, x3] とすると、以下のように表せることを確かめよ。
AX = XA = I
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

# デコレータを定義
def solve_for_multiple_b(func):
    def wrapper(A, b_list):
        solutions = []
        for b in b_list:
            solutions.append(func(A, b))
        return solutions
    return wrapper

@solve_for_multiple_b
def solve_linear_system(A, b):
    """LU分解を用いて連立方程式を解く"""
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

# 行列Aとbのリスト
A = np.array([[1, 2, 3], [1, 3, 3], [2, 5, 7]], dtype=float)
b_list = [
    np.array([1, 0, 0], dtype=float),
    np.array([0, 1, 0], dtype=float),
    np.array([0, 0, 1], dtype=float)
]

# 解を求める
solutions = solve_linear_system(A, b_list)

# 結果をx1, x2, x3に代入
x1, x2, x3 = solutions

# 結果を表示
"""
以下の連立方程式(演習問題5.2)行列Aとベクトルx,bで表し、LU分解を用いて解を求めよ。
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * x1 = [1, 0, 0]^t
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * x2 = [0, 1, 0]^t
  [[1, 2, 3], [1, 3, 3], [2, 5, 7]] * x3 = [0, 0, 1]^t
"""
print(f"Solution vector x1: \n{x1}\n")
print(f"Solution vector x2: \n{x2}\n")
print(f"Solution vector x3: \n{x3}\n")

"""
X = [x1, x2, x3] とすると、以下のように表せることを確かめよ。
AX = XA = I
"""
X = np.array([x1, x2, x3]).T
I = np.eye(3)

print(f"A: \n{A}\n")
print(f"X: \n{X}\n")

print(f"AX: \n{np.dot(A, X)}\n")
print(f"XA: \n{np.dot(X, A)}\n")
print(f"I: \n{I}\n")

