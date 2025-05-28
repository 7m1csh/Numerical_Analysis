# 演習問題 6.3 チェビシェフ多項式の漸化式計算
print("\n演習問題 6.3 チェビシェフ多項式の漸化式計算")
print(
"""
チェビシェフ多項式の漸化式を用いて、T5(x)を求めよ。
x^2 及び x^3 をチェビシェフ多項式で表せ。
また、以下の式を用いて、x=1 でのチェビシェフ多項式の値を4次まで求めよ。
Tn(x) = 2xTn-1(x) - Tn-2(x)
"""
)

import sympy as sp

# チェビシェフ多項式の漸化式を定義
# チェビシェフ多項式 Tn(x) の漸化式を文字式で求める
def chebyshev_recursive(n, x):
    if n == 0:
        return 1  # T0(x) = 1
    elif n == 1:
        return x  # T1(x) = x
    else:
        Tn_minus_2 = chebyshev_recursive(n - 2, x)
        Tn_minus_1 = chebyshev_recursive(n - 1, x)
        return sp.expand(2 * x * Tn_minus_1 - Tn_minus_2)

# T5(x)を文字式で求める
x = sp.symbols('x')

T5 = chebyshev_recursive(5, x)
print(f"T5(x) = {T5}")
print()

# x^2 と x^3 をチェビシェフ多項式で表す
T2 = chebyshev_recursive(2, x)
T3 = chebyshev_recursive(3, x)
print(f"x^2 = {T2}")
print(f"x^3 = {T3}")
print()

# x=1 でのチェビシェフ多項式の値を4次まで求める
for n in range(1, 5):
    Tn_at_1 = chebyshev_recursive(n, 1)
    print(f"T{n}(1) = {Tn_at_1}")
# 出力結果を表示


