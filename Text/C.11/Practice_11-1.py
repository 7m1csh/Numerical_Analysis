# Practice 11.1 台形による定積分の近似

import numpy as np
import matplotlib.pyplot as plt

# 積分対象の関数
def f(x):
    return np.sin(x)

# 積分区間
a = 0
b = np.pi
n = 5  # 分割数（台形の数）

# 台形の幅
h = (b - a) / n

# xの分割点
x = np.linspace(a, b, n + 1)
y = f(x)

# 台形公式による近似積分
integral_approx = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])

# 描画用の滑らかな曲線
x_fine = np.linspace(a, b, 400)
y_fine = f(x_fine)

# プロット
plt.figure(figsize=(10, 6))
plt.plot(x_fine, y_fine, 'b', label='f(x) = sin(x)')
plt.fill_between(x, y, step='mid', alpha=0.3, color='orange', label='Trapezoids')
for i in range(n):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, y[i], y[i+1], 0]
    plt.fill(xs, ys, 'orange', edgecolor='black', alpha=0.5)

plt.title('Approximation of Integral using Trapezoidal Rule')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

