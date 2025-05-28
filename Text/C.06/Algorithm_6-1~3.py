# Algorithm 6.1, 6.2, 6.3 多項式の和、積、割り算
"""
6.1 h(x) = f(x) + g(x)
6.2 h(x) = f(x)g(x)
6.3 f(x) = q(x)g(x) + r(x)
"""

import sympy as sp

def polynomial_addition(f, g):
    """多項式の和を計算する"""
    n = max(len(f), len(g))
    f = [0] * (n - len(f)) + f  # 高次の順にゼロ埋め
    g = [0] * (n - len(g)) + g  # 高次の順にゼロ埋め
    h = [f[i] + g[i] for i in range(n)]
    return h

def polynomial_multiplication(f, g):
    """多項式の積を計算する"""
    n = len(f) + len(g) - 1
    h = [0] * n
    for i in range(len(f)):
        for j in range(len(g)):
            h[i + j] += f[i] * g[j]
    return h

def polynomial_division(f, g):
    """多項式の割り算を計算する"""
    if len(g) == 0 or (len(g) == 1 and g[0] == 0):
        raise ValueError("g(x) cannot be zero polynomial")
    
    f = f[:]  # コピーを作成
    q = []
    
    while len(f) >= len(g):
        coeff = f[0] / g[0]
        q.append(coeff)
        # g(x) を coeff 倍して f から引く
        for i in range(len(g)):
            f[i] -= coeff * g[i]
        f.pop(0)  # 先頭のゼロを削除
    
    # 余りを返す（高次の順に整形）
    return q, f

# 多項式の入力
def input_polynomial(prompt):
    while True:
        try:
            coeffs = input(prompt).strip().split(',')
            return [float(c) for c in coeffs]
        except ValueError:
            print("無効な入力です。係数をカンマ区切りで入力してください。")

def main():
    f = input_polynomial("f(x)の係数を高次の順にカンマ区切りで入力してください: ")
    g = input_polynomial("g(x)の係数を高次の順にカンマ区切りで入力してください: ")

    # sympyを使用して多項式を表示
    x = sp.symbols('x')
    f_poly = sum(c * x**i for i, c in enumerate(reversed(f)))
    g_poly = sum(c * x**i for i, c in enumerate(reversed(g)))
    print("f(x):", f_poly)
    print("g(x):", g_poly)

    # 6.1 多項式の和
    h_add = polynomial_addition(f, g)
    h_add_poly = sum(c * x**i for i, c in enumerate(reversed(h_add)))
    print("h(x) = f(x) + g(x):", h_add_poly)

    # 6.2 多項式の積
    h_mul = polynomial_multiplication(f, g)
    h_mul_poly = sum(c * x**i for i, c in enumerate(reversed(h_mul)))
    print("h(x) = f(x) * g(x):", h_mul_poly)

    # 6.3 多項式の割り算
    q, r = polynomial_division(f, g)
    q_poly = sum(c * x**i for i, c in enumerate(reversed(q)))
    r_poly = sum(c * x**i for i, c in enumerate(reversed(r)))
    print("q(x):", q_poly)
    print("r(x):", r_poly)
    print("f(x) = q(x)g(x) + r(x):", f_poly, "=", q_poly, "*", g_poly, "+", r_poly)

if __name__ == "__main__":
    main()

