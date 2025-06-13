# 演習問題 8.2 f(x)=x^2 - a のニュートン法による反復式
"""
関数 f(x)=x^2 - a のニュートン法による反復式をsympyを用いて表示する。
また、a = 2 とし、初期値x0 = 1.0 として、反復を行い、x1, x2, x3 の値を求める。
同時に 各近似解における真値np.sqrt(2) との誤差も求め表示する。
"""
import sympy as sp
import numpy as np

# シンボリック変数の定義
x, a = sp.symbols('x a')
# 関数 f(x) の定義
f_x = x**2 - a
# ニュートン法の反復式の導出
f_prime_x = sp.diff(f_x, x)  # f(x) の導関数
newton_iteration = x - f_x / f_prime_x
# ニュートン法の反復式を表示
print("ニュートン法の反復式:")
print(f" x = {sp.simplify(newton_iteration)}")
    
def newton_method(a, x0, iterations=3):
    x = x0
    results = []
    
    for i in range(iterations):
        f_x = x**2 - a
        f_prime_x = 2 * x
        x_new = x - f_x / f_prime_x
        error = np.abs(np.sqrt(a) - x_new)
        
        results.append((x_new, error))
        x = x_new
    
    return results

# 初期値とパラメータの設定
a = 2
x0 = 1.0
# ニュートン法の実行
results = newton_method(a, x0)
# 結果の表示
for i, (x_new, error) in enumerate(results):
    print(f"x{i+1} = {x_new}, 誤差 = {error}")
# 出力例
# x1 = 1.5, 誤差 = 0.41421356237309515
# x2 = 1.4166666666666667, 誤差 = 0.09807621135331646
# x3 = 1.4142156862745099, 誤差 = 0.0000021311475411442904

