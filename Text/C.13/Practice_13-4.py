import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 係数行列 A と定数ベクトル b
A = np.array([[-2.0, 1.0],
              [ 1.0, 1.0]])
b = np.array([0.0, 3.0])

# 初期解
x = np.array([1.0, 3.0])
history = [x.copy()]

# ヤコビ法のための係数分解
D = np.diag(np.diag(A))
R = A - D
D_inv = np.linalg.inv(D)

# 反復
for i in range(10):
    x = np.dot(D_inv, b - np.dot(R, x))
    history.append(x.copy())

history = np.array(history)

# 描画
x_vals = np.linspace(0, 4, 400)
y1 = 2 * x_vals          # -2x1 + x2 = 0 → x2 = 2x1
y2 = 3 - x_vals          # x1 + x2 = 3 → x2 = 3 - x1

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1, label=r"$-2x_1 + x_2 = 0$")
plt.plot(x_vals, y2, label=r"$x_1 + x_2 = 3$")
plt.plot(history[:, 0], history[:, 1], 'o-', color='red', label='反復解')
plt.xlim(0, 3.5)
plt.ylim(0, 3.5)
plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")
plt.legend()
plt.grid(True)
plt.title("ヤコビ法による反復解と方程式の交点")
plt.show()

