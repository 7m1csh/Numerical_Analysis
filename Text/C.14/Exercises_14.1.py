# 演習問題 14.1
"""
以下の行列について、CRS形式（CSR形式）で示せ。
A = [[-2, 1, 0, 0],
     [ 1,-2, 1, 0],
     [ 0, 1,-2, 1],
     [ 0, 0, 1,-2]
    ]
"""

from scipy.sparse import csr_matrix
import numpy as np

A = [[-2, 1, 0, 0],
     [ 1,-2, 1, 0],
     [ 0, 1,-2, 1],
     [ 0, 0, 1,-2]
    ]

csr_A = csr_matrix(A)
a = csr_A.data.tolist()
c = csr_A.indices.tolist()
r = csr_A.indptr.tolist()

print(f"行列 A :\n{np.array(A)}\n")
print("CSR形式に変換したときの非ゼロ要素ベクトル　a =", a)
print("CSR形式に変換したときの列インデックス　　　c =", c)
print("CSR形式に変換したときの位置ポインター　　　r =", r)

