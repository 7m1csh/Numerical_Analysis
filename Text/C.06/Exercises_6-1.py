# 演習問題 6.1 多項式の計算
"""
多項式 f(x)=x^3-x^2-2x+3, g(x)=x^2-3x+2 に対して、
f(x)+g(x), f(x)g(x), 及びf(x)をg(x)で割った商q(x)とあまりr(x)を求めよ。
"""

from sympy import symbols, expand, simplify, div

# 記号の定義
x = symbols('x')

# 関数定義（f(x), g(x)）
f = x**3 - x**2 - 2*x + 3
g = x**2 - 3*x + 2

# 1. 和 h(x) = f(x) + g(x)
h_add = f + g

# 2. 積 h(x) = f(x) * g(x)
h_mul = expand(f * g)

# 3. 商と余り q(x), r(x) such that f(x) = g(x) * q(x) + r(x)
q, r = div(f, g)  # div は Euclidean division を返す

# 表示
print("\n演習問題 6.1 多項式の計算\n")
print("f(x) =", f)
print("g(x) =", g)
print("f(x) + g(x) =", h_add)
print("f(x) * g(x) =", h_mul)
print("商 q(x) =", q)
print("余り r(x) =", r)

