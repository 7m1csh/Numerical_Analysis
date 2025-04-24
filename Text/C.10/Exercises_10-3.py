# 演習問題 10.3
"""
a1 = [1, 1, 1]^t
a2 = [-1, 0, 1]^t
A = [a1, a2]
A^T A の固有値分解を行い、特異値分解を求めよ。
"""

import numpy as np

# Aの定義（a1, a2を列ベクトルとして結合）
a1 = np.array([1, 1, 1])
a2 = np.array([-1, 0, 1])
A = np.column_stack((a1, a2))  # 3x2 行列

# AtA の固有値分解
AtA = A.T @ A
eigvals, V = np.linalg.eigh(AtA)  # 固有値（昇順）、固有ベクトル列（右特異ベクトル）

# 特異値（固有値の平方根）
singular_values = np.sqrt(np.maximum(eigvals, 0))  # 数値誤差で負になるのを防ぐ

# 左特異ベクトル U の計算
U = np.zeros((A.shape[0], A.shape[1]))
for i in range(A.shape[1]):
    if singular_values[i] > 1e-10:
        U[:, i] = A @ V[:, i] / singular_values[i]

# U, Σ, V^T の確認
Sigma = np.diag(singular_values)

print("A:")
print(A)
print("\nA^T A:")
print(AtA)
print("\n固有値:")
print(eigvals)
print("\n特異値:")
print(singular_values)
print("\n右特異ベクトル V（列ベクトル）:")
print(V)
print("\n左特異ベクトル U（列ベクトル）:")
print(U)
print("\n再構成 A ≈ U @ Σ @ V^T:")
print(U @ Sigma @ V.T)

