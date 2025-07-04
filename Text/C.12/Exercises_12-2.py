# 演習問題 12.2 ホイン法による u'=t+u u(0)=1,h=0.1 u(0.1), u(0.2) の近似値を求める
"""
u' = t + u,  u(0) = 1 に対して、h = 0.1 として、ホイン法により、
u(0.1), u(0.2) の近似値を求めよ。
なお、解析解は、$u(t) = -t - 1 + 2e^t$ である。
・u(t)のグラフを描く
・t=0.1, t=0.2 からグラフ上に垂線を引き、u(t) と交わった値をグラフ上に明記する。
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# 微分方程式の右辺 f(t, u) = t + u
def f(t, u):
    return t + u

# 初期条件
t0 = 0.0  # 初期時刻
u0 = 1.0  # 初期値
h = 0.1  # ステップサイズ

# 時間の範囲
t_values = np.arange(t0, 0.3, h)  # 0.0 から 0.2 までの値

# ホイン法の計算
u_values = [u0]  # 初期値をリストに追加
for i in range(len(t_values) - 1):
    t_n = t_values[i]
    u_n = u_values[i]
    
    # ホイン法の2段階計算
    # 第1段階：予測子（オイラー法による予測）
    u_predict = u_n + h * f(t_n, u_n)
    
    # 第2段階：修正子（傾きの平均を使用）
    u_next = u_n + h * (f(t_n, u_n) + f(t_n + h, u_predict)) / 2
    
    u_values.append(u_next)

# ホイン法結果の表示
print("ホイン法の計算結果")
print(f"u(0.1) = {u_values[1]:.6f}")
print(f"u(0.2) = {u_values[2]:.6f}")

print()

# 解析解の計算
def analytical_solution(t):
    return -t - 1 + 2 * np.exp(t)

# 解析解の値を計算
analytical_values = [analytical_solution(t) for t in t_values]

# 解析解での結果の表示
print("解析解での計算結果")
print(f"u(0.1) = {analytical_values[1]:.6f}")
print(f"u(0.2) = {analytical_values[2]:.6f}")

print()

# 誤差の計算と表示
print("誤差の計算")
error_01 = abs(u_values[1] - analytical_values[1])
error_02 = abs(u_values[2] - analytical_values[2])
print(f"u(0.1)の誤差 = {error_01:.6f}")
print(f"u(0.2)の誤差 = {error_02:.6f}")

# より細かい時間軸でのグラフ描画用
t_fine = np.linspace(0, 0.2, 100)
u_fine = [analytical_solution(t) for t in t_fine]

# グラフの描画
plt.figure(figsize=(12, 8))
plt.plot(t_fine, u_fine, label='解析解', color='blue', linewidth=2)
plt.plot(t_values, u_values, label='ホイン法', marker='o', color='red', markersize=8, linewidth=2)
plt.xlabel("t", fontsize=12)
plt.ylabel("u(t)", fontsize=12)

# t=0.1, t=0.2 の垂線を描画
plt.axvline(x=0.1, color='gray', linestyle='--', alpha=0.7, label='t = 0.1')
plt.axvline(x=0.2, color='gray', linestyle='--', alpha=0.7, label='t = 0.2')

# ホイン法の点を強調
plt.scatter([0.1, 0.2], [u_values[1], u_values[2]], color='red', s=100, zorder=5)

# 解析解の点を強調
plt.scatter([0.1, 0.2], [analytical_values[1], analytical_values[2]], color='blue', s=100, zorder=5)

# 値の表示
plt.text(0.1, u_values[1] + 0.05, f"ホイン法: {u_values[1]:.4f}", color='red', fontsize=10, ha='center')
plt.text(0.2, u_values[2] + 0.05, f"ホイン法: {u_values[2]:.4f}", color='red', fontsize=10, ha='center')

plt.text(0.1, analytical_values[1] - 0.05, f"解析解: {analytical_values[1]:.4f}", color='blue', fontsize=10, ha='center')
plt.text(0.2, analytical_values[2] - 0.05, f"解析解: {analytical_values[2]:.4f}", color='blue', fontsize=10, ha='center')

plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.title("ホイン法と解析解の比較 (u' = t + u, u(0) = 1)", fontsize=14)
plt.tight_layout()
plt.show()

# 計算過程の詳細表示
print("\n計算過程の詳細:")
print("=" * 50)
u_temp = u0
for i in range(2):  # t=0.1, t=0.2まで
    t_n = t_values[i]
    u_n = u_temp
    
    print(f"\nステップ {i+1}: t = {t_n:.1f} から t = {t_n+h:.1f}")
    print(f"u({t_n:.1f}) = {u_n:.6f}")
    
    # 第1段階：予測子
    k1 = f(t_n, u_n)
    u_predict = u_n + h * k1
    print(f"予測子: u_predict = {u_n:.6f} + {h:.1f} × {k1:.6f} = {u_predict:.6f}")
    
    # 第2段階：修正子
    k2 = f(t_n + h, u_predict)
    u_next = u_n + h * (k1 + k2) / 2
    print(f"修正子: u({t_n+h:.1f}) = {u_n:.6f} + {h:.1f} × ({k1:.6f} + {k2:.6f})/2 = {u_next:.6f}")
    
    u_temp = u_next
