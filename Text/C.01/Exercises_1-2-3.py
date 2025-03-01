# 演習問題１−2
"""
計算量がnの3乗に比例する方法を用いて計算機で計算したとき、
n=5で1秒で結果が得られた。実行時間は計算量のみに依存する
としたとき、n=15では何秒かかると予想されるか。
※計算量がnの階乗に比例する方法のn=10の場合は、Exercises_1-2-1.py
※計算量がnの階乗に比例する方法のn=15の場合は、Exercises_1-2-2.py
"""

import matplotlib.pyplot as plt

def calculate_time(n):
    # n=5のとき1秒かかると仮定し、それを基準に他のnの値に対する時間を計算
    return (n**3) / (5**3)

# nの値の範囲を1から15に設定
n_values = range(1, 16)

# 各nに対する計算時間を計算
times = [calculate_time(n) for n in n_values]

# グラフをプロット
plt.figure(figsize=(12, 7))
plt.plot(n_values, times, marker='o')
plt.title('Relationship between n and Calculation Time (O(n³))')
plt.xlabel('n')
plt.ylabel('Calculation Time (seconds)')
plt.grid(True)

# 各点にラベルを付ける
for i, (n, t) in enumerate(zip(n_values, times)):
    if n % 3 == 0 or n == 1:  # n が 3 の倍数または 1 の場合にラベルを表示
        plt.annotate(f'n={n}\nt={t:.2f}s', (n, t), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()

# 結果を表示
print("n\tCalculation Time (seconds)")
for n, t in zip(n_values, times):
    print(f"{n}\t{t:.2f}")

