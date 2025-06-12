# Algorithm 8.2 割線法

import math

def secant_method(f, x0, x1, epsilon=1e-8, k_max=20):
    print("反復\t近似値\t\t誤差")
    f0 = f(x0)
    for k in range(2,k_max):
        if abs(f(x1) - f(x0)) < 1e-14:
            print("割線の傾きが0に近づいたため停止")
            break
        f1 = f(x0)
        fe = abs(f1)
        if fe <= epsilon:
            break
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        print(f"{k}\t{x2:.10f}\t{fe:.1e}")
        x0, x1 = x1, x2
        f0 = f1
    return x2

f = lambda x: x**2 - 2

secant_method(f, 1.0, 2.0)

