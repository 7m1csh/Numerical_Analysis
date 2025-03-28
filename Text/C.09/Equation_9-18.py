# (9.18) 

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.sparse import diags

# 三重対角行列の主対角成分と副対角成分
b = np.array([4, 4, 4, 4])   # 主対角成分
a = np.array([1, 1, 1])      # 下副対角成分（対称なので上副対角成分も同じ）
T = diags([a, b, a], offsets=[-1, 0, 1]).toarray()

# scipy の三重対角行列専用の固有値計算関数
eigenvalues, eigenvectors = eigh_tridiagonal(b, a)

print(f"三重対角行列 T:\n{T}\n")
print(f"固有値 l:\n{eigenvalues}\n")
print(f"固有ベクトル行列 X:\n{eigenvectors}\n")

L = diags([eigenvalues], offsets=[0]).toarray()
print(f"固有値を対角成分に持つ行列(固有値行列)L:\n{L}\n")

# TX と XR がほぼ等しいことを確認
TX = T @ eigenvectors
XL = eigenvectors @ L
print(f"T ✕ X:\n{TX}\n\nX ✕ L:\n{XL}\n")

