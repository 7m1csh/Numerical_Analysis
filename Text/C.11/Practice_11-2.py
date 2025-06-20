# Practice 11.2 ガウス則

import numpy as np

# 2点ガウス求積則を使って ∫_{-1}^{1} f(x) dx を近似する
def fs(x):
    return np.sin(x)  # 任意の関数

def fc(x):
    return np.cos(x)  # 任意の関数

# 2点ガウス則の節点と重み（[-1, 1] に固定）
x_gauss = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
w_gauss = np.array([1.0, 1.0])

# sin積分近似
approx_integral = np.sum(w_gauss * fs(x_gauss))

# 真の値（sin(x) の [-1, 1] における定積分値）
true_integral = -np.cos(1) + np.cos(-1)

print("2点ガウス求積則を使って ∫ _{-1}^{1} f(x) dx を近似する\n")

# 結果
print(f"2点ガウス則によるf(x)=sin(x)の近似：{approx_integral}\n真の値：{true_integral}\n誤差：{abs(approx_integral - true_integral)}")

print()

# cos積分近似
approx_integral = np.sum(w_gauss * fc(x_gauss))

# 真の値（cos(x) の [-1, 1] における定積分値）
true_integral = np.sin(1) - np.sin(-1)

print(f"2点ガウス則によるf(x)=cos(x)の近似：{approx_integral}\n真の値：{true_integral}\n誤差：{abs(approx_integral - true_integral)}")
