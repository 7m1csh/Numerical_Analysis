# Practice 7.3 ニュートン補間
# 3点補間 (1, 2), (2, 3), (3, 5)

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 補間点
x_points = np.array([1, 2, 3])
y_points = np.array([2, 3, 5])

# 差分商テーブルを作る関数
def divided_differences(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:] = (coef[j:] - coef[j-1:-1]) / (x[j:] - x[:n-j])
    return coef

# 補間多項式の定義
def newton_polynomial(x, x_data, coef):
    n = len(coef)
    result = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x - x_data[j])
        result += term
    return result

# 差分商係数の計算
coefficients = divided_differences(x_points, y_points)
print("ニュートン補間の係数:", coefficients)

# プロット
x_vals = np.linspace(0, 4, 200)
y_vals = newton_polynomial(x_vals, x_points, coefficients)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="ニュートン補間多項式", color="blue")
plt.scatter(x_points, y_points, color="red", label="補間点")
plt.title("ニュートン補間")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

