# Gram Schimdt 直交化法の練習プログラム

import numpy as np

def gram_schmidt(V):
    """
    グラム・シュミットの直交化法を実装
    入力: V (行列: 各行がベクトル)
    出力: 直交ベクトルの集合 U
    """
    V = np.array(V, dtype=np.float64)
    n, m = V.shape  # n: ベクトルの数, m: 次元数
    U = np.zeros((n, m))
    
    for i in range(n):
        u_i = V[i]
        for j in range(i):
            if np.dot(U[j], U[j]) != 0:
                proj = np.dot(U[j], V[i]) / np.dot(U[j], U[j]) * U[j]
                u_i -= proj
        U[i] = u_i
    
    return U

# 使用例
V = [[1, 1], [1, 2]]  # ベクトル集合
U = gram_schmidt(V)
print("直交化されたベクトル:")
print(U)

