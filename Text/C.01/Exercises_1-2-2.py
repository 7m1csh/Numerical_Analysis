# 演習問題 (2)
"""
計算量がnの階乗に比例する方法を用いて計算機で計算したとき、
n=5で1秒で結果が得られた。実行時間は計算量のみに依存する
としたとき、n=15では何秒かかると予想されるか。
※n=10の場合は、Exercises_1-2-1.py
※nの3乗の場合は、Exercises_1-2-3.py
"""

import math
import matplotlib.pyplot as plt

def calculate_time(n):
    # n=5のとき1秒かかると仮定し、それを基準に他のnの値に対する時間を計算
    return math.factorial(n) / math.factorial(5)

# nの値の範囲を1から15に拡張
n_values = range(1, 16)

# 各nに対する計算時間を計算
times = [calculate_time(n) for n in n_values]

# グラフをプロット
plt.figure(figsize=(12, 7))
plt.plot(n_values, times, marker='o')
plt.title('Relationship between n and Calculation Time')
plt.xlabel('n')
plt.ylabel('Calculation Time (seconds)')
plt.yscale('log')  # y軸を対数スケールに設定
plt.grid(True)

# 各点にラベルを付ける（ただし、見やすさのために一部の点のみ）
for i, (n, t) in enumerate(zip(n_values, times)):
    if n % 3 == 0 or n == 1:  # n が 3 の倍数または 1 の場合にラベルを表示
        plt.annotate(f'n={n}\nt={t:.2e}s', (n, t), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()

# 結果を表示
print("n\tCalculation Time (seconds)")
for n, t in zip(n_values, times):
    print(f"{n}\t{t:.2e}")

