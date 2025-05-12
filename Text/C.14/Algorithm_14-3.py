# Algorithm 14.3 共役勾配法

import numpy as np
from numpy.linalg import norm

def conjugate_gradient(A, b, x0=None, epsilon=1e-8, max_iter=None):
    n = len(b)

    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()

    if max_iter is None:
        max_iter = n

    r = b - A @ x
    p = r.copy()

    for i in range(max_iter):
        Ap = A @ p
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r1 = r - alpha * Ap
        if norm(r1) < epsilon * norm(b):
            break
        beta = np.dot(r1, r1) / np.dot(r, r)
        r = r1
        p = r + beta * p

    return x, i + 1

# 使用例
A = np.array([
    [4, 1, 0],
    [1, 3, 0],
    [0, 0, 2]
], dtype=float)

b = np.array([1, 2, 0], dtype=float)
x0 = np.zeros_like(b)

solution, num_iter = conjugate_gradient(A, b, x0, epsilon=1e-8)

print(f"連立方程式 Ax=b :\nA:\n{A}\n\nb={b}^t\n")
print("解 x =", solution)
print("反復回数 =", num_iter)

