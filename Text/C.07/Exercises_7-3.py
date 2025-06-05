# 演習問題 7.3 ニュートン補間
"""
3点、x0,x1,及びx2が与えられたとき、
ニュートン補間係数関数をsympyを用いて文字列式で出力する。
また、f(x0)=y0, f(x1)=y1, 及びf(x2)=y2 の場合のニュートン補間を求める。
x及びyは"(x0,x1,x2) : " "(y0,y1,y2) : "の形でキー入力させ、簡単な例外処理を付加する。
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def newton_interpolation(x_values, y_values, print_diff=False):
    x = sp.symbols('x')
    n = len(x_values)
    
    # 差分商を計算するためのテーブル
    divided_diff = [y_values[:]]  # 初期値はy_values
    
    # 差分商の計算と表示
    if print_diff:
        print("差分商:")
        print(f"0階差分商: {divided_diff[0]}")  # 0階差分商（y値）
    
    for j in range(1, n):
        diff = []
        for i in range(n - j):
            diff.append((divided_diff[j-1][i+1] - divided_diff[j-1][i]) / (x_values[i+j] - x_values[i]))
        divided_diff.append(diff)
        if print_diff:
            print(f"{j}階差分商: {diff}")  # 各階の差分商を表示
    
    # ニュートン補間多項式の構築
    P = divided_diff[0][0]  # 最初の項
    for j in range(1, n):
        term = divided_diff[j][0]  # j次の差分商
        for k in range(j):
            term *= (x - x_values[k])  # (x - x_k)の積
        P += term
    
    return sp.simplify(P)

def plot_interpolation(x_values, y_values, polynomial):
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 100)
    y = [polynomial.evalf(subs={sp.symbols('x'): xi}) for xi in x]

    plt.plot(x, y, label='Newton Interpolation')
    plt.scatter(x_values, y_values, color='red', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Newton Interpolation')
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

        # x値が重複している場合はエラー
        if len(set(x_values)) != len(x_values):
            raise ValueError("xの値はすべて異なる必要があります。")

        # ニュートン補間を計算（差分商を表示）
        result = newton_interpolation(x_values, y_values, print_diff=True)
        print("ニュートン補間結果:", result)

        # 結果をグラフ表示（差分商の表示は抑制）
        plot_interpolation(x_values, y_values, result)

    except Exception as e:
        print("エラー:", e)
 
if __name__ == "__main__":
    main()
