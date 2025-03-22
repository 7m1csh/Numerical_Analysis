# modified cholesky decomposition

import numpy as np

def modified_cholesky(A, epsilon=1e-10):
    """修正Cholesky分解: A = LDL^T (Lは下三角行列, Dは対角行列)"""
    n = A.shape[0]
    L = np.zeros_like(A)
    D = np.zeros(n)

    # A の対角成分が正であることを保証
    A_mod = A + epsilon * np.eye(n)

    for j in range(n):
        temp_sum = np.sum(L[j, :j] ** 2 * D[:j])
        D[j] = A_mod[j, j] - temp_sum

        # もし D[j] が負またはゼロなら、小さい正の値を足して補正
        if D[j] <= 0:
            D[j] = epsilon
        
        L[j, j] = 1  # 対角成分は 1
        for i in range(j + 1, n):
            temp_sum = np.sum(L[i, :j] * L[j, :j] * D[:j])
            L[i, j] = (A_mod[i, j] - temp_sum) / D[j]

    return L, np.diag(D)

# テスト用の行列（正定値対象行列）
A = np.array([[4, 2], [2, 3]], dtype=float)

L, D = modified_cholesky(A)
print("テスト用の行列 A:")
print(A)
print("")

print("修正Cholesky分解 L:")
print(L)
print("")

print("対角行列 D:")
print(D)
print("")

print("再構成 A = L D L^T:")
print(L @ D @ L.T)

