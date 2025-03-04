#Algorithm 2.4 モンテカルロ法による円周率の計算
"""
テキストでは、n個の配列に予め乱数を格納しておく方法が紹介されているが、
繰り返しの都度乱数を生成し計算するほうがメモリの節約になる。
"""

import random
import math

def estimate_pi(n):
    num_point_circle = 0    # 円内に入った点の数(テキストではm)
    num_point_total = 0     # 点の総数(テキストではn)
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1
    return 4 * num_point_circle / num_point_total


# コンソールからの入力
while True:
    try:
        n = int(input("繰り返しの回数を入力してください: "))
        if n <= 0:
            raise ValueError("正の整数である必要があります。")
        break
    except ValueError as e:
        print(f"エラー: {e}. 正の整数を入力してください。")

# 結果の出力
p = estimate_pi(n)
print(p)

