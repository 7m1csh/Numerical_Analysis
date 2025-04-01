# 演習問題 9.2
"""
行列 A = [[2, -1], [-1, 2]] とする。
ベクトル y = [4, 1]^t について、
y = c1*x1 + c2x*2 となる、c1, c2 を求めよ。
x1, x2 はAの固有ベクトルとする。
"""

import numpy as np
from scipy.linalg import eig

A = np.array([[2, -1], [-1, 2]])
y = np.array([4, 1])

# 固有値と固有ベクトルを求める
eigenvalues, eigenvectors = eig(A)

# 固有値と固有ベクトルを実数化（虚数部分がゼロの場合のみ）
eigenvalues = np.real(eigenvalues)
eigenvectors = np.real(eigenvectors)

# 固有ベクトルを正規化
eigenvectors = eigenvectors / np.linalg.norm(eigenvectors, axis=0)

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
print()

# c1, c2 を求める
c1 = np.dot(y, eigenvectors[:, 0])
c2 = np.dot(y, eigenvectors[:, 1])
print("c1: ", c1)
print("c2: ", c2)
print("y = %f * x1 + %f * x2" % (c1, c2))
print()

# 確認
print("ライブラリを使った確認")
reconstructed_y = c1 * eigenvectors[:, 0] + c2 * eigenvectors[:, 1]
print(f"y = {reconstructed_y}")
