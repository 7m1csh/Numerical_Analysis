# 演習問題 7.4 パデ近似

import sympy
from sympy.abc import x
from sympy import Poly # Polyをインポート

def pade_approximation_manual_exp(a, n):
    """
    exp(x)のマクローリン展開を用いて、x=aにおけるx^nの項までのパデ近似式を求めます。
    sympy.rational_approximationが利用できない場合の代替実装。

    Args:
        a (float): 展開の中心点（実数）。（この関数では直接使用せず、x=0のマクローリン展開を元にパデ近似を生成します）
        n (int): マクローリン展開の項数（正の整数）。x^nの項まで。

    Returns:
        sympy.Expr or None: パデ近似式のsympy文字列式。入力が不正な場合はNone。
    """
    if not isinstance(a, (int, float)):
        print("エラー: 'a'は実数である必要があります。")
        return None
    if not isinstance(n, int) or n <= 0:
        print("エラー: 'n'は正の整数である必要があります。")
        return None

    # exp(x)のマクローリン展開を取得し、オーダー項を削除
    # n+1 次までの項が必要 (P(x) の次数 m と Q(x) の次数 k の合計が n)
    # series(x, 0, n+1) は x^n の係数まで計算し、O(x^(n+1)) を追加する
    maclaurin_series_expr = sympy.exp(x).series(x, 0, n + 1).removeO()

    # マクローリン展開の係数を取得する際にPolyを使うことで、確実に係数を抽出
    # Poly(式, 変数) で多項式オブジェクトを作成し、coeffsリストから係数を取得
    # Poly.coeffs() は最高次の項から最低次の項へ係数を返すため、逆順にする
    try:
        poly_maclaurin = Poly(maclaurin_series_expr, x)
        # coeffs は [c_0, c_1, ..., c_n] の順になるように逆順に並べ替える
        coeffs = poly_maclaurin.all_coeffs()[::-1]
        # n+1 個の係数があることを確認 (c_0 から c_n まで)
        if len(coeffs) <= n: # もし係数が足りない場合は、不足分を0で埋める
             coeffs.extend([0] * (n + 1 - len(coeffs)))
        # 余分な係数があれば切り捨てる (n+1個まで)
        coeffs = coeffs[:n+1]
    except Exception as e:
        print(f"マクローリン展開の係数取得中にエラーが発生しました: {e}")
        return None

#    print(f"DEBUG: coeffs = {coeffs}") # 追加

    # パデ近似式の分子と分母の次数を設定
    # P(x) の次数 m, Q(x) の次数 k, m + k = n
    m = n // 2  # 分子の次数
    k = n - m   # 分母の次数

#    print(f"DEBUG: m={m}, k={k}") # 追加

    # Q(x) = q0 + q1*x + ... + qk*x^k (q0 = 1と仮定)
    # P(x) = p0 + p1*x + ... + pm*x^m

    # q_1, ..., q_k を求めるための k 個の連立方程式
    # Q(x) * f(x) - P(x) = O(x^(n+1))
    # 係数c_iはcoeffsリストに格納されている

    # q_0 = 1 と仮定し、以下の連立方程式を解いて q_1, ..., q_k を求める
    # sum_{j=0}^{k} q_j * c_{i-j} = 0 for i = m+1, ..., n
    # (但し、q_0 = 1)
    # sum_{j=1}^{k} q_j * c_{i-j} = -c_i for i = m+1, ..., n

    # 行列 A とベクトル B を構築 (A * q_vec = B)
    # q_vec は [q_1, q_2, ..., q_k]
    A = sympy.Matrix.zeros(k, k)
    B = sympy.Matrix.zeros(k, 1)

    for row_idx in range(k):
        # 連立方程式の i は m+1 から n まで
        current_i = m + 1 + row_idx

        # B の要素: -c_i
        # coeffsリストが current_i まで存在するかチェック
        if current_i < len(coeffs):
            B[row_idx, 0] = -coeffs[current_i]
        else:
            B[row_idx, 0] = 0 # 係数が存在しない場合は0

        # A の要素: q_j の係数 c_{i-j}
        for col_idx in range(k):
            # q_{col_idx+1} の係数
            coeff_index_in_c = current_i - (col_idx + 1)
            # coeffsリストが coeff_index_in_c まで存在するかチェック
            if coeff_index_in_c >= 0 and coeff_index_in_c < len(coeffs):
                A[row_idx, col_idx] = coeffs[coeff_index_in_c]
            else:
                # 存在しない係数は0
                A[row_idx, col_idx] = 0

#    print(f"DEBUG: A = {A}") # 追加
#    print(f"DEBUG: B = {B}") # 追加

    # q_vec = [q_1, ..., q_k] を解く
    try:
        # k=0 (分母が定数) の場合、AとBは空行列になるので、LUsolveは適用できない
        if k == 0:
            q_solution = sympy.Matrix([]) # 空の行列として扱う
        else:
            q_solution = A.LUsolve(B)
    except Exception as e:
        print(f"分母係数(q)の連立方程式の解でエラーが発生しました。nの値が小さすぎるか、パデ近似が適切でない可能性があります。エラー: {e}")
        return None

#    print(f"DEBUG: q_solution = {q_solution}") # 追加

    q_coeffs = [sympy.S(1)] # q_0 = 1
    for val in q_solution:
        q_coeffs.append(val)
#    print(f"DEBUG: q_coeffs = {q_coeffs}") # 追加

    # p_0, ..., p_m を求める
    # p_i = sum_{j=0}^{min(i, k)} q_j * c_{i-j} for i = 0, ..., m
    p_coeffs = []
    for i in range(m + 1):
        p_val = sympy.S(0)
        for j in range(min(i, k) + 1):
            if i - j >= 0 and (i - j) < len(coeffs) and j < len(q_coeffs): # 係数リストの範囲チェックを追加
                p_val += q_coeffs[j] * coeffs[i - j]
            # else: 係数が存在しない場合は加算しない（0として扱われる）
        p_coeffs.append(p_val)
#    print(f"DEBUG: p_coeffs = {p_coeffs}") # 追加

    # 多項式を構築
    numerator = sympy.S(0)
    for i, p_val in enumerate(p_coeffs):
        numerator += p_val * x**i

    denominator = sympy.S(0)
    for i, q_val in enumerate(q_coeffs):
        denominator += q_val * x**i

    return numerator / denominator

if __name__ == "__main__":
    while True:
        try:
            a_str = input("展開の中心点 'a' を入力してください (実数): ")
            a = float(a_str)
            break
        except ValueError:
            print("無効な入力です。'a'は実数で入力してください。")

    while True:
        try:
            n_str = input("マクローリン展開の項数 'n' を入力してください (正の整数): ")
            n = int(n_str)
            if n <= 0:
                print("無効な入力です。'n'は正の整数で入力してください。")
            else:
                break
        except ValueError:
            print("無効な入力です。'n'は整数で入力してください。")

    # 手動実装の関数を呼び出す
    pade_result = pade_approximation_manual_exp(a, n)

    if pade_result:
        print(f"\nexp(x)の{n}次のマクローリン展開から導出されたパデ近似式 (x=0の周り):")
        # 結果が非常に複雑になる場合があるので、simplifyを試みる
        simplified_pade = sympy.simplify(pade_result)

        # LaTeX形式での表示
        print(f"Pade({n}) = {sympy.latex(simplified_pade)}")
        # 通常の文字列形式での表示
        print(f"Pade({n}) = {simplified_pade}")
