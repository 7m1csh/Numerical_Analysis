# Algorithm 14.2 CRS(CSR)形式の行列ベクトル積y=A^txの計算

from scipy.sparse import csr_matrix
import numpy as np

# デモ用御用列のデータ
A = [[ 5,  0,  0, -1,  0],
     [ 0,  3,  9,  0,  0],
     [ 0,  0,  1,  0,  8],
     [ 0, -2,  0,  5,  0],
     [-3,  0,  0,  2, -1]]

csr_A = csr_matrix(A)
a = csr_A.data.tolist()
c = csr_A.indices.tolist()
r = csr_A.indptr.tolist()

#デモ用行列をCSR形式に変換したデータ（期待値）
#a = [5, -1, 3, 9, 1, 8, -2, 5, -3, 2, -1]
#c = [0, 3, 1, 2, 2, 4, 1, 3, 0, 3, 4]
#r = [0, 2, 4, 6, 8, 11]

# デモ用ベクトル x
x = [1, 2, 1, 1, 1]

# 表示
print(f"デモ用行列 A :\n{np.array(A)}\n")
print(f"デモ用行列 A^t :\n{np.array(A).T}\n")
print("CSR形式に変換したときの非ゼロ要素ベクトル　a =", a)
print("CSR形式に変換したときの列インデックス　　　c =", c)
print("CSR形式に変換したときの位置ポインター　　　r =", r)
print(f"デモ用ベクトル x : {x}\n")

# 行数
n = len(r) - 1

# 結果ベクトル y の初期化
y = [0] * n

# 行列ベクトル積の計算
for j in range(n):
    for i in range(r[j], r[j+1]):
        y[c[i]] += a[i] * x[j]

# 結果表示
print(f"Algorithm 14.2 で計算した A^tx = y = {y}")
print(f"numpyを使って計算した     A^tx = y = {(np.array(A).T@np.array(x).T).tolist()}")

