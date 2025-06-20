# Algorithm 11.1 複合台形則

import numpy as np

# 関数定義
def f(x):
    return np.sin(x)

# 複合台形則の実装
def composite_trapezoidal_rule(f, a, b, N):
    h = (b - a) / N
    I = f(a) / 2
    for j in range(1,N):
        I = I + f(a+h*j)
    I = I + f(b) / 2
    I = I * h
    return I

# パラメータ
a = 0
b = np.pi
n = 10

# 複合台形則による近似積分
approx_integral = composite_trapezoidal_rule(f, a, b, n)

# 真の値（解析的な積分値）
true_value = 2.0  # ∫₀^π sin(x) dx = 2

# 結果表示
print(f"複合台形則による計算値：{approx_integral}\n真の値：{true_value}\n誤差：{abs(approx_integral - true_value)}")

