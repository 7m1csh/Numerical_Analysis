# 行列の相似変換

import numpy as np
import matplotlib.pyplot as plt

# 2x2行列の対角化
A = np.array([[4, 1], [-2, 1]])
print(f"以下の行列 A を相似変換で対角化する: \n{A}\n")

# 固有値と固有ベクトルの計算
eigenvalues, eigenvectors = np.linalg.eig(A)

# 固有値を昇順にソートし、それに対応するインデックスを取得
sorted_indices = np.argsort(eigenvalues)

# 固有値と対応する固有ベクトルを並べ替え
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

print("eigenvalues = ", eigenvalues)
print("eigenvectors = \n", eigenvectors)

# 固有ベクトルを列ベクトルとして取り出す
v1 = eigenvectors[:, 0]
v2 = eigenvectors[:, 1]

# 固有ベクトルをスケーリング（第1成分を1に固定）
v1 = (v1 / v1[0]).round().astype(int)
v2 = (v2 / v2[0]).round().astype(int)
print("固有ベクトルをスケーリング（第1成分を1に固定）")
print("v1 (スケーリング修正) = ", v1)
print("v2 (スケーリング修正) = ", v2)
print()

# 相似変換を行う
P = np.array([v1, v2]).T
P_inv = np.linalg.inv(P)
D = np.diag(eigenvalues)
A_prime = P @ D @ P_inv

print(f"固有ベクトルを並べた行列 P を作る:\n{P}\n")
print(f"P の逆行列 P_inv :\n{P_inv}\n")
print(f"相似変換で得られた対角行列（固有値を対角成分に並べた行列） D :\n{D}\n")
print(f"検証 A' = P D P^t:\n{A_prime}\n")

# 固有ベクトルを描画
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v2')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()

