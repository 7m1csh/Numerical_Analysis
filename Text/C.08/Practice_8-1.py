# Practice 8.1 不動点近傍の反復の様子
import numpy as np
import matplotlib.pyplot as plt

# 関数の定義
def g(x):
    return np.cos(x)

# 反復の初期値
#x0 = 0.5
x0 = 0.2
iterations = 10

# 軸の範囲
x_vals = np.linspace(0, 1.5, 300)
y_vals = g(x_vals)

# グラフの準備
plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, label=r'$y = g(x)$', color='blue')
plt.plot(x_vals, x_vals, label=r'$y = x$', color='gray', linestyle='--')

# 反復過程（くもの巣）
x = x0
for _ in range(iterations):
    y = g(x)
    # 縦線： (x, x) → (x, g(x))
    plt.plot([x, x], [x, y], color='red')
    # 横線： (x, g(x)) → (g(x), g(x))
    plt.plot([x, y], [y, y], color='red')
    x = y

# 描画設定
plt.title('Cobweb Plot: Fixed-Point Iteration for $g(x) = \cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

