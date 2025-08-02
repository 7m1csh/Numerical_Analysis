# 演習問題 13.4

from sympy import Matrix, symbols, eye, solve, sqrt

# 記号 lambda を定義
lam = symbols('lambda')

# 3重対角行列を定義
A = Matrix([
    [-2, 1, 0, 0],
    [1, -2, 1, 0],
    [0, 1, -2, 1],
    [0, 0, 1, -2]
])

print("与えられた行列 A:")
print(A)
print("-" * 30)

# 固有方程式 A - lambda * I を計算
# I は単位行列
n = A.shape[0] # 行列のサイズを取得
I = eye(n) # サイズ n の単位行列を作成
characteristic_matrix = A - lam * I

print("固有方程式 A - lambda * I:")
print(characteristic_matrix)
print("-" * 30)

# 固有多項式 det(A - lambda * I) を計算
characteristic_polynomial = characteristic_matrix.det()

print("固有多項式 det(A - lambda * I):")
print(characteristic_polynomial)
print("-" * 30)

# 固有多項式 = 0 を解いて固有値を求める
# solve 関数は、与えられた式の根 (roots) を求めます。
eigenvalues_symbolic = solve(characteristic_polynomial, lam)

print("固有多項式 = 0 を解いて得られた固有値 (記号表現と数値近似):")
for val in eigenvalues_symbolic:
    # evalf() メソッドで数値近似を計算
    numerical_val = val.evalf()
    print(f"{val} = {numerical_val:.5f}") # 小数点以下5桁で表示
print("-" * 30)
