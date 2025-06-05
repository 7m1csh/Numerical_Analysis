# Exercises 7.1 マクローリン近似
"""
半径rの円に内接する正5角形の一辺の長和長さはl=2r*sin(π/5)である。
sin(x)の3次までのマクローリン展開を用いて、r=10のときのlの近似値を求めよ。
"""

import math

def maclaurin_sin(x, n_terms=1): #問題文が曖昧だがx^3の項までを期待してるようなのでn_term=1
    """
    マクローリン展開を用いてsin(x)を近似する関数
    :param x: 近似したい角度（ラジアン）
    :param n_terms: 使用する項の数
    :return: sin(x)の近似値
    """
    sin_approx = 0
    for n in range(n_terms+1):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        print(f"sin({x}) 展開第{n}次の項 = {term}")
        sin_approx += term
    return sin_approx

def calculate_length(r):
    """
    半径rの円に内接する正5角形の一辺の長さを計算する関数
    :param r: 円の半径
    :return: 正5角形の一辺の長さ
    """
    angle = math.pi / 5  # 5角形の内角
    print(f"π/ 5 = {angle}")
    sin_value = maclaurin_sin(angle)  # マクローリン展開によるsin値の近似
    length = 2 * r * sin_value  # 一辺の長さ
    return length

# 半径r=10のときの正5角形の一辺の長さを計算
r = 10
length_approx = calculate_length(r)
print(f"半径{r}の円に内接する正5角形の一辺の長さの近似値: {length_approx:.4f}")


