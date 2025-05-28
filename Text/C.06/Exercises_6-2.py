# 演習問題 6.2 多項式の値をホーナー法で求める
"""
多項式 f(x)=x^3-x^2-2x+3 に対して、
x=2 における値 f(2) をホーナー法で求めよ。
また、その導関数値、及び二次導関数値を求めよ。
"""

from sympy import symbols, Poly
from Algorithm0604 import horner
from Algorithm0605 import extended_horner 

# 記号の定義
x = symbols('x')

print("\n演習問題 6.2 多項式の値をホーナー法で求める\n")

# 関数定義f(x)
f = x**3 - x**2 - 2*x + 3
print(f"f(x) = {f}")

# fを係数リストに変換
coeffs = Poly(f, x).all_coeffs()

# f(2)の計算
f_value = horner(coeffs, 2)
print(f"f(2) = {f_value}")

# f'(2)の計算
f1_value = extended_horner(coeffs, 2, 1)
f1_value = [float(v) for v in f1_value]
print(f"f'(2) = {f1_value}")

# f''(2)の計算
f2_value = extended_horner(coeffs, 2, 2)
f2_value = [float(v) for v in f2_value]
print(f"f''(2) = {f2_value}")
