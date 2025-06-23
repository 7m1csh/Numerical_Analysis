# 演習問題 11.4 2点ガウス型積分則
"""
区間 $[-1,1]$ において、 $x_0 = \frac {-1}{\sqrt(3)}, x_1 = \frac {1}{\sqrt(3)}$ とする。
$x_0, x_1$ を積分点とする積分則の重み $\alpha_0, \alpha_1$ を求めよ。
この積分則を $x^k, k=1,2,3$ に適用せよ。
"""

import sympy as sp

# シンボル定義
x = sp.Symbol('x')
x0 = -1 / sp.sqrt(3)
x1 = 1 / sp.sqrt(3)

# ラグランジュ補間基底関数 w_0(x), w_1(x)
w0 = (x - x1) / (x0 - x1)
w1 = (x - x0) / (x1 - x0)

# 積分区間 [-1, 1]
a, b = -1, 1

# α_j = ∫ w_j(x) dx over [-1, 1]
alpha_0 = sp.integrate(w0, (x, a, b)).evalf()
alpha_1 = sp.integrate(w1, (x, a, b)).evalf()

# 積分則を x^k (k = 1,2,3) に適用
f_values = {}
for k in [1, 2, 3]:
    f = x**k
    approx = alpha_0 * f.subs(x, x0) + alpha_1 * f.subs(x, x1)
    exact = sp.integrate(f, (x, a, b)).evalf()
    f_values[f"x^{k}"] = (exact, approx.evalf())

print(f"積分則の重みα0 = {alpha_0}, α1 = {alpha_1}")

# 辞書の内容を1行ずつ出力
for key, value in f_values.items():
    print(f"{key}: 真値 = {value[0]}, 計算値 = {value[1]}")

