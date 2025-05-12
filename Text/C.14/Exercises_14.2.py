# 演習問題 14.2
"""
行列AがCRS形式（CSR形式）で
a = [2,-1,-1,2,-1,-1,2]
c = [1,2,1,2,3,2,3]
r = [1,3,6,8]
で与えられるとき、Aを密行列の形で示せ。
また、このCSR形式を用いて
ベクトル x = [-1,0,1]^t に対して
Aとの外積を計算して過程を示せ。
"""

from scipy.sparse import csr_matrix
import numpy as np

# CRS形式の行列を作成
a = np.array([2, -1, -1, 2, -1, -1, 2])
c = np.array([0, 1, 0, 1, 2, 1, 2])
r = np.array([0, 2, 5, 7])

# CRS形式から密行列に変換
A = csr_matrix((a, c, r), shape=(3, 3)).toarray()
print(f"密行列 A:\n{A}\n")

# ベクトル x
x = np.array([-1, 0, 1])

# 外積を計算
Ax = A @ x
print(f"Ax: {Ax}\n")

# 結果を表示
print("Ax の要素:")
for i in range(len(Ax)):
    print(f"Ax[{i}] = {Ax[i]}")

