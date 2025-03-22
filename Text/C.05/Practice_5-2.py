# cholesky decomposition

import numpy as np

def cholesky_decomposition(A):
    """Cholesky分解: A = LL^T"""
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)

    for i in range(n):
        for j in range(i+1):
            if i == j:  # 対角成分
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :j] ** 2))
            else:  # 非対角成分
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    
    return L

# 例
A = np.array([[4, 2], [2, 3]], dtype=float)
L = cholesky_decomposition(A)

print("A:")
print(A)
print("")

print("L:")
print(L)
print("")

print("L @ L.T:")
print(L @ L.T)  # A に戻るか確認

