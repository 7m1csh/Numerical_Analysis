# 演習問題 4.1
"""
行列A,B,及びベクトルxを次のように指定する。
A=[[1, 1], [1, 0]]
B=[[1, 1], [0, 1]]
x=[1, 0]T
(A^^2)x  (A^^3)x  A(Ax)  A(A(Ax)) を求めよ。
また、(AB)T  BTAT  tr(AB)  tr(BA) を求めよ。
"""

import numpy as np

# 行列とベクトルの定義
A = np.array([[1, 1], [1, 0]])
B = np.array([[1, 1], [0, 1]])
x = np.array([[1], [0]])  # 列ベクトル

## 第1部：行列累乗とベクトル積の計算
# A^2x
A2x = np.linalg.matrix_power(A, 2) @ x

# A^3x
A3x = np.linalg.matrix_power(A, 3) @ x

# A(Ax)
Ax = A @ x
A_Ax = A @ Ax

# A(A(Ax))
A_A_Ax = A @ (A @ (A @ x))

## 第2部：行列演算の性質確認
# (AB)^T
AB_T = (A @ B).T

# B^T A^T
BT_AT = B.T @ A.T

# トレース計算
tr_AB = np.trace(A @ B)
tr_BA = np.trace(B @ A)

## 結果表示
print("=== 定義 ===")
print(f"A = \n{A}")
print(f"B = \n{B}")
print(f"x = \n{x}")
print("")

print("=== 第1部: 行列累乗とベクトル積 ===")
print(f"A²x = \n{A2x}")
print(f"A³x = \n{A3x}")
print(f"A(Ax) = \n{A_Ax}")
print(f"A(A(Ax)) = \n{A_A_Ax}\n")

print("=== 第2部: 行列演算の性質 ===")
print(f"(AB)^T = \n{AB_T}")
print(f"B^T A^T = \n{BT_AT}")
print(f"tr(AB) = {tr_AB}")
print(f"tr(BA) = {tr_BA}")

