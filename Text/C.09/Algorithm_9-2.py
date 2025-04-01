# Algorithm 9.2 レイリー・リッツ手法

import numpy as np

# --- 1. 対称行列 A の定義 ---
A = np.array([[4, 1, 2],
              [1, 3, 0],
              [2, 0, 5]])

# --- 2. 基底ベクトルの選択（部分空間の定義） ---
"""
(1, 0, 1)^T と (0, 1, 1)^T という2つの独立なベクトルを使って、
3次元空間内の2次元部分空間を構成する。
これにより、元の行列 A の固有値の一部を近似できる。
"""
V = np.array([[1, 0],
              [0, 1],
              [1, 1]], dtype=float)

# --- 3. 直交化（グラム・シュミット法） ---
# V の列を直交化し、直交行列 Q を作る
Q, _ = np.linalg.qr(V)

# --- 4. 射影行列 Am = Q^T A Q の計算 ---
Am = Q.T @ A @ Q

# --- 5. Am の固有値を求める ---
eigvals_Am, eigvecs_Am = np.linalg.eig(Am)

# --- 6. 元の行列 A の固有値を求める ---
eigvals_A, eigvecs_A = np.linalg.eig(A)

# --- 7. 結果の表示 ---
print("元の行列 A の固有値:", eigvals_A)
print("レイリー・リッツ手法による近似固有値:", eigvals_Am)

