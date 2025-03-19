# Gaussian elimination with partial pivot selection

import numpy as np

def gauss_elim_pivoting(A, b):
    n = len(b)
    
    for k in range(n-1):
        # 軸選択（部分ピボット選択）
        max_row = np.argmax(np.abs(A[k:n, k])) + k
        if A[max_row, k] == 0:
            raise ValueError("行列は特異行列であり、解が一意に定まりません。")
        
        # 行の入れ替え
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[k], b[max_row] = b[max_row], b[k]

        for i in range(k+1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]

    return A, b

# Example
A = np.array([[1, 2, 3], [1, 3, 3], [2, 5, 7]], dtype=float)
b = np.array([1, 2, 2], dtype=float)

print("Original matrix A :")
print(A)
print("Original vector b :")
print(b)
print("")

A_pivoted, b_pivoted = gauss_elim_pivoting(A.copy(), b.copy())

print("Updated matrix A (with pivoting):")
print(A_pivoted)
print("Updated vector b (with pivoting):")
print(b_pivoted)

