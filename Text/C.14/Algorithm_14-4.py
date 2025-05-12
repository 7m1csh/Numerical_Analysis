# Algorithm 14.4 前処理付き共役勾配法

import numpy as np

def pcg_jacobi(A, b, x0=None, epsilon=1e-8, max_iter=None):
    n = len(b)
    A = np.array(A)
    b = np.array(b)

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0)

    # Jacobi前処理行列の逆: C^{-1} = diag(1/A_ii)
    C_inv = 1.0 / np.diag(A)

    r = b - A @ x
    z = C_inv * r  # C^{-1} * r
    p = z

    if max_iter is None:
        max_iter = n * 10

    for k in range(max_iter):
        Ap = A @ p
        alpha = np.dot(z, r) / np.dot(p, Ap)
        x = x + alpha * p
        r1 = r - alpha * Ap

        if np.linalg.norm(r1) < epsilon * np.linalg.norm(b):
            break

        z1 = C_inv * r1
        beta = np.dot(z1, r1) / np.dot(z, r)
        z = z1
        r = r1
        p = z + beta * p

    return x, k + 1

# 正定値対称行列 A(2x2)
A = [[4, 1],
     [1, 3]]
b = [1, 2]
x0 = [0.0, 0.0]

print(f"連立方程式 Ax=b :\nA:\n{A}\n\nb={b}^t\n")
print(f"初期解 x0 = {x0}\n")

x, iterations = pcg_jacobi(A, b, x0, epsilon=1e-10)
print("解 x =", x)
print("反復回数 =", iterations)

