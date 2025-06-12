# Algorithm 8.1 ニュートン法

import numpy as np

# 関数と導関数
f = lambda x: x - np.cos(x)
df = lambda x: 1 + np.sin(x)
true_fx = 0.739085133215

def newton_method(f, df, x0, epsilon=1e-10, kmax=20):
    x = x0
    print(f"反復回数\t近似解\t\t\t絶対誤差\t残差")
    for k in range(kmax):
        if abs(df(x)) < 1e-14:
            print("導関数が 0 に近いため停止")
            return None

        f0 = f(x)
        print(f"{k}\t\t{x:.15f}\t{abs(true_fx - x):.1e}\t\t{abs(f0):.1e}")

        if abs(f0) < epsilon:
            break

        f1 = df(x)
        x = x - f0 / f1
    return x

# 初期値
root = newton_method(f, df, x0=0.25)
print(f"近似解: {root:.15f}")

