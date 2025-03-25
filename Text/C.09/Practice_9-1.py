# Practice 9.1 余因子行列の計算

import numpy as np

# 行列 A の定義
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("元の行列:\n", A, "\n")

# 余因子行列 C の計算
C = np.zeros((3, 3))  # 余因子行列の初期化

for i in range(3):
    for j in range(3):
        # A の (i, j) 成分を除いた小行列の行列式を計算し、符号を調整
        minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
        C[i, j] = (-1) ** (i + j) * np.linalg.det(minor)

# 結果の表示
print("余因子行列:\n", C)

