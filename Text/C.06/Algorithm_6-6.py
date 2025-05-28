# Algorithm 6.6 拡張ユークリッド算法

from sympy import symbols, div, Poly, simplify

# 記号の定義
x = symbols('x')

# 多項式 f(x), g(x)
F = Poly(x**3 - x**2 - 2*x + 2, x)
G = Poly(x**2 - 3*x + 2, x)

# 初期表示
print(f"初期値:")
print(f"f(x) = {F.as_expr()}")
print(f"g(x) = {G.as_expr()}\n")

# 初期化
f = [F, G]  # f[0] = F, f[1] = G
A = [Poly(1, x), Poly(0, x)]  # A[0] = 1, A[1] = 0
B = [Poly(0, x), Poly(1, x)]  # B[0] = 0, B[1] = 1
q = []  # 商を格納するリスト

k = 1
while not f[k].is_zero:
    # 商と剰余を計算
    quotient, remainder = div(f[k-1], f[k], domain='QQ')
    q.append(quotient)  # 商をリストに追加
    f.append(remainder)  # 剰余をリストに追加

    # A[k+1] と B[k+1] を計算
    A.append(A[k-1] - q[k-1] * A[k])
    B.append(B[k-1] - q[k-1] * B[k])

    # 結果を表示
    print(f"  q({k}) = {q[k-1]}")
    print(f"  f({k}) = {f[k]}")
    print(f"  A({k}) = {A[k]}")
    print(f"  B({k}) = {B[k]}")
    print("")

    # 次のステップへ
    k += 1

l = k - 1  # 最後の非ゼロ剰余のインデックス

# 結果の表示
print(f"=== 結果 ===")
print(f"gcd(f, g) = f(l) = {f[l].as_expr()}")
print(f"A(l) = {A[l].as_expr()}")
print(f"B(l) = {B[l].as_expr()}")

# 検算
lhs = simplify(F.as_expr()*A[l].as_expr() + G.as_expr()*B[l].as_expr())
print(f"\n確認: f(x)*A(x) + g(x)*B(x) = {lhs}")

