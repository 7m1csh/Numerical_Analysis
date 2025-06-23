# 演習問題 11.2 ラグランジュ補間に基づく数値積分則（ニュートン・コーツ型積分則）の重み（係数）を求める
"""
$x_0=0, x_1=1/2, x_2=1$ とし、これらを補間点とするラグランジュ補間多項式の
区間 $[0,1]$ における定積分から、以下の積分則
$$I=\alpha_0f(x_0)+\alpha_1f(x_1)+\alpha_2f(x_2)$$
の重み $\alpha_0, \alpha_1, \alpha_2$ を求めよ。
ここで、ラグランジュ補間係数関数は、
$$w_j(x) = \prod_{\substack{i=0 \\ i \ne j}}^n \frac{x - x_i}{x_j - x_i}$$
で与えられたとき、$\alpha_j$ は、
$$\alpha_j = \int_a^b w_j(x)\,dx$$
で求められる。
"""

from scipy.integrate import quad

# 各 w_j(x) を定義

def w0(x):
    return ((x - 0.5) * (x - 1)) / 0.5

def w1(x):
    return -4 * x * (x - 1)

def w2(x):
    return 2 * x * (x - 0.5)

# 各 α_j を積分
alpha_0, _ = quad(w0, 0, 1)
alpha_1, _ = quad(w1, 0, 1)
alpha_2, _ = quad(w2, 0, 1)

print(f"α_0 = {alpha_0}")
print(f"α_1 = {alpha_1}")
print(f"α_2 = {alpha_2}")
print(f"α_0 + α_1 + α_2 = {alpha_0 + alpha_1 + alpha_2}")

