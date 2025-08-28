# Practice 15.3 並列化率やプロセッサ数を変化させた加速比のグラフ
#               グスタフソンの法則

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# アムダールの法則の関数
"""
def amdahl_speedup(P, N):
    return 1 / ((1 - P) + P / N)
"""

# グスタフソンの法則
def gustafson_speedup(P, N):
    return N - (1 - P) * (N - 1)

# プロセッサ数の範囲
N_values = np.arange(1, 129)

# 並列化率のリスト
P_values = [0.5, 0.75, 0.9, 0.95, 0.99]

plt.figure(figsize=(8, 6))

# 各並列化率ごとに加速比を計算してプロット
for P in P_values:
    speedup = gustafson_speedup(P, N_values)
    plt.plot(N_values, speedup, label=f"P = {P*100:.0f}%")

plt.xlabel("プロセッサ数 N")
plt.ylabel("加速比 S(N)")
plt.title("グスタフソンの法則による加速比の限界")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

