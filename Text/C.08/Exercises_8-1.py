# 演習問題 8.1 ニュートン法の反復式
"""
関数 f(x) = 1 / x - a のニュートン法による反復式をsympyを用いてx(k+1)=x(x)..の形式で求める。
また、 a = 3 のとき、初期値を x0 = 1 /2 として、1回の反復した近似解 x1 を求める。
つづいて、x2, x3 を求める。
"""

import sympy as sp
# シンボリック変数の定義
x, a = sp.symbols('x a')
# 関数 f(x) の定義
f = 1 / x - a
# ニュートン法の反復式の導出
f_prime = sp.diff(f, x)  # f(x) の導関数
newton_iteration = x - f / f_prime  # ニュートン法の反復式
# ニュートン法の反復式を x(k+1) = x(k)... の形式に変形
newton_iteration_simplified = sp.simplify(newton_iteration)
# ニュートン法の反復式を表示
print("ニュートン法の反復式: x =", newton_iteration_simplified)
# a = 3 のときの近似解を求める
a_value = 3
x0 = 1 / 2  # 初期値
# 1回目の反復
x1 = newton_iteration_simplified.subs({x: x0, a: a_value})
# 2回目の反復
x2 = newton_iteration_simplified.subs({x: x1, a: a_value})
# 3回目の反復
x3 = newton_iteration_simplified.subs({x: x2, a: a_value})
# 結果の表示
print(f"近似解 x1 = {x1.evalf()}")
print(f"近似解 x2 = {x2.evalf()}")
print(f"近似解 x3 = {x3.evalf()}")

