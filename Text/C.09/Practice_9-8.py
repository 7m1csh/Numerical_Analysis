# Practice 9.8 Householder変換による三重対角化

import numpy as np
from scipy.linalg import hessenberg

# 任意の対称行列
A = np.array([[4, 1, 2, 3],
              [1, 4, 3, 2],
              [2, 3, 4, 1],
              [3, 2, 1, 4]])

# Householder変換で三重対角行列を求める
T, Q = hessenberg(A, calc_q=True)

# 数値誤差をゼロに補正
T[np.abs(T) < 1e-10] = 0

# 固有値を計算
eig_A = np.linalg.eigvals(A)
eig_A[np.abs(eig_A) < 1e-10] = 0  # 数値誤差をゼロに補正

eig_T = np.linalg.eigvals(T)
eig_T[np.abs(eig_T) < 1e-10] = 0  # 数値誤差をゼロに補正

# 三重対角行列を作るために使用したユニタリ行列∋ハウスホルダー行列
QtQ = Q.T @ Q
QtQ[np.abs(QtQ) < 1e-10] = 0

print("Practice 9.8 Householder変換による三重対角化\n")
print(f"対称行列 A :\n{A}\n")
print(f"A を三重対角行列するために使うユニタリ行列 ∋ ハウスホルダー行列 Q (A = Q @ T @ Q^t):\n{Q}\n")
print(f"三重対角行列 T :\n{T}\n")
print("元の行列 A の固有値    :", np.sort(eig_A))
print("三重対角行列 T の固有値:", np.sort(eig_T))
print("")
print(f"Q の直交性確認　Q^t @ Q = I :\n{QtQ}\n")
print(f"Q のエルミート性確認　Q* = Q :\n{np.conj(Q.T)}")
