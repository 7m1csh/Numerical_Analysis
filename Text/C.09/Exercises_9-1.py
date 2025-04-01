# 演習問題 9.1
"""
行列 A = [[2, -1], [-1, 2]] とする。
A の特性多項式の零点を求めることで、固有値e1,e2を求めよ。
(A-e1)x1=0 の関係を用いて、固有ベクトルx1を求めよ。
このとき、||x1||2 = 1 とせよ。同様にx2を求めよ。
"""

import numpy as np
from scipy.linalg import eig

# 行列 A の特性多項式の零点を求める
# e^2 - 4e + 3 = 0
e1 = 1
e2 = 3
x1 = np.array([1, 1])
x2 = np.array([1, -1])
x1 = x1 / np.linalg.norm(x1)
x2 = x2 / np.linalg.norm(x2)
print("手計算による結果")
print("固有値: ", e1, e2)
print("固有ベクトル: ", x1, x2)
print()

A = np.array([[2, -1], [-1, 2]])
eigenvalues, eigenvectors = eig(A)
print("ライブラリによる結果")
print("固有値: ", eigenvalues)
print("固有ベクトル:\n", eigenvectors)

