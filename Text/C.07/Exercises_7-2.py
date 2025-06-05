# 演習問題 7.2 ラグランジュ補間
"""
3点、x0,x1,及びx2が与えられたとき、
ラグランジュ補間係数関数をsympyを用いて文字列式で出力する。
また、f(x0)=y0, f(x1)=y1, 及びf(x2)=y2 の場合のラグランジュ補間を求める。
x及びyは"(x0,x1,x2) : " "(y0,y1,y2) : "の形でキー入力させ、簡単な例外処理を付加する。
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values):
    x = sp.symbols('x')
    n = len(x_values)
    L = 0

    for i in range(n):
        # ラグランジュ基底多項式
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
        L += y_values[i] * L_i

    return sp.simplify(L)

def plot_interpolation(x_values, y_values):

    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 100)
    y = [lagrange_interpolation(x_values, y_values).evalf(subs={sp.symbols('x'): xi}) for xi in x]

    plt.plot(x, y, label='Lagrange Interpolation')
    plt.scatter(x_values, y_values, color='red', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Lagrange Interpolation')
    plt.legend()
    plt.ylim(min(y_values) - 1, max(y_values) + 1)
    plt.grid()
    plt.show()
 
def main():
    try:
        x_input = input("(x0,x1,x2) : ")
        y_input = input("(y0,y1,y2) : ")

        # 入力をパース
        x_values = list(map(float, x_input.strip('()').split(',')))
        y_values = list(map(float, y_input.strip('()').split(',')))

        if len(x_values) != 3 or len(y_values) != 3:
            raise ValueError("3つの値を入力してください。")

        # ラグランジュ補間を計算
        result = lagrange_interpolation(x_values, y_values)
        print("ラグランジュ補間結果:", result)

    except Exception as e:
        print("エラー:", e)

    # 結果をグラフ表示する
    plot_interpolation(x_values, y_values)
 
if __name__ == "__main__":
    main()

