# 演習問題 11.3 台形則とシンプソン則の比較
"""
(1)関数、$f(x) = 1, f(x) = x, f(x) = x^2$ の区間 $[0,1]$ における
積分の近似値を台形則、及びシンプソン則で求めよ。

(2)以下の積分を台形則とシンプソンで近似せよ。
$$f(x) = \int_0^1 \frac{1}{1+x^2}\,dx = \frac {\pi}{4}$$
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 台形則の実装
def trapezoidal(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

# シンプソン則の実装
def simpson(f, a, b):
    c = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4*f(c) + f(b))

# 対象関数（ベクトル対応で定義）
functions = {
    "f(x) = 1": lambda x: np.ones_like(x),
    "f(x) = x": lambda x: x,
    "f(x) = x^2": lambda x: x**2,
    "f(x) = 1 / (1 + x^2)": lambda x: 1 / (1 + x**2),
}

a, b = 0, 1  # 積分区間

# 可視化準備
x = np.linspace(a, b, 400)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.flatten()

results = []

for i, (label, f) in enumerate(functions.items()):
    fx = f(x)
    ax = axs[i]
    ax.plot(x, fx, label=label, color='black')
    ax.set_title(label)
    ax.set_xlim(a, b)
    ax.set_ylim(0, max(fx) * 1.2)
    ax.fill_between(x, 0, fx, color='skyblue', alpha=0.3)

    # 台形則の可視化
    xt = np.array([a, b])
    yt = f(xt)
    ax.plot(xt, yt, 'o-', color='red', label='Trapezoid')

    # シンプソン則の可視化
    xm = (a + b) / 2
    ym = f(np.array([xm]))[0]
    ax.plot([a, xm, b], [f(np.array([a]))[0], ym, f(np.array([b]))[0]], 'o--', color='green', label='Simpson')

    # 数値値計算
    trap = trapezoidal(lambda x: f(np.array([x]))[0], a, b)
    simp = simpson(lambda x: f(np.array([x]))[0], a, b)
    exact, _ = quad(lambda x: f(np.array([x]))[0], a, b)
    results.append((label, exact, trap, simp))

    ax.legend()

plt.tight_layout()

# 結果をテキストでまとめる
results_text = "関数\t\t\t真値\t\t台形則\t\tシンプソン則\n" + "-"*68 + "\n"
for label, exact, trap, simp in results:
    results_text += f"{label:<20}\t{exact:.6f}\t{trap:.6f}\t{simp:.6f}\n"

# 結果を表示
print(results_text)

# グラフを表示
plt.show()

