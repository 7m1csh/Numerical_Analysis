# Algorithm 5.2 LU分解(軸選択なし)

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

# テスト
A = np.array([[2, 3, 1], [4, 7, 3], [6, 18, 5]], dtype=float)
L, U = lu_decomposition(A)

print("L:")
print(L)
print("U:")
print(U)

