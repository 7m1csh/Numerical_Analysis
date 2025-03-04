# Algorithm 2.3 二分法
"""
二分法による f(x)=0 の近似解の計算
"""

import sympy as sp

def bisection_method(f, a, b, d):
    while abs(b - a) > d:
        c = (a + b) / 2
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
    return (a + b) / 2

# f(x)の入力
fx_str = input("f(x) を入力してください（例：x**2 - 2 ）: ")

# a, b, dの入力
a = float(input("aの値を入力してください（例：1 or 1.0 ）: "))
b = float(input("bの値を入力してください（例：2 or 2.0 ）: "))
d = float(input("dの値を入力してください（例：1e-6 or 0.000001 ）: "))

# SymPyを使用してf(x)を評価可能な関数に変換
x = sp.Symbol('x')
fx_expr = sp.sympify(fx_str)
f = sp.lambdify(x, fx_expr)

# 2分法の実行
result = bisection_method(f, a, b, d)

print(f"\n近似解: {result}")
print(f"f({result}) = {f(result)}")

