# 数式(8.28) f(x) = (x-1)(x-2)...(x-20)

import numpy as np
import sympy

# シンボル変数を定義
x = sympy.Symbol('x')

# 関数と導関数
f_sym = (x-1)*(x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7)*(x-8)*(x-9)*(x-10)*(x-11)*(x-12)*(x-13)*(x-14)*(x-15)*(x-16)*(x-17)*(x-18)*(x-19)*(x-20)
df_sym = sympy.diff(f_sym,x)

# sympyの式をnumpyの関数に変換
f = sympy.lambdify(x, f_sym, 'numpy')
df = sympy.lambdify(x, df_sym, 'numpy')

def newton_method(f, df, x0, true_fx, epsilon=1e-10, kmax=20):
    x = x0
    print(f"反復回数\t近似解\t\t\t相対誤差\t残差")
    for k in range(kmax):
        if abs(df(x)) < 1e-14:
            print("導関数が 0 に近いため停止")
            return None

        f0 = f(x)
        fe = abs((x - true_fx) / true_fx)
        print(f"{k}\t\t{x:.15f}\t{fe:.1e}\t\t{abs(f0):.1e}")

        if abs(f0) < epsilon:
            break

        f1 = df(x)
        x = x - f0 / f1
    return x

# x0=1.1の近似解
print("ニュートン法の計算結果（x0=1.1 ）")
root = newton_method(f, df, x0=1.1, true_fx=1.0)
print(f"近似解: {root:.15f}")

print()


print("ニュートン法の計算結果（x0=15.1 ）")
root = newton_method(f, df, x0=15.1, true_fx=15.0)
print(f"近似解: {root:.15f}")

