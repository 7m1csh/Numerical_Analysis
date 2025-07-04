# 演習問題 12.1 オイラー法による u'=t+u u(0)=1,h=0.1 u(0.1), u(0.2) の近似値を求める
"""
u' = t + u,  u(0) = 1 に対して、h = 0.1 として、オイラー法により、
u(0.1), u(0.2) の近似値を求めよ。
なお、解析解は、$u(t) = -t - 1 + 2e^t$ である。
・u(t)のグラフを描く
・t=0.1, t=0.2 からグラフ上に垂線を引き、u(t) と交わった値をグラフ上に明記する。
"""

import numpy as np
import matplotlib.pyplot as plt

# 初期条件
t0 = 0.0  # 初期時刻
u0 = 1.0  # 初期値
h = 0.1  # ステップサイズ

# 時間の範囲
t_values = np.arange(t0, 0.3, h)  # 0.0 から 0.2 までの値

# オイラー法の計算
u_values = [u0]  # 初期値をリストに追加
for t in t_values[:-1]:  # 最後の値は計算しない
    u_next = u_values[-1] + h * (t + u_values[-1])  # オイラー法の更新式
    u_values.append(u_next)  # 次の値をリストに追加

# オイラー法結果の表示
print("オイラー法の計算結果")
print(f"u(0.1) = {u_values[1]:.4f}")
print(f"u(0.2) = {u_values[2]:.4f}")

print()

# 解析解の計算
def analytical_solution(t):
    return -t - 1 + 2 * np.exp(t)

# 解析解の値を計算
analytical_values = [analytical_solution(t) for t in t_values]

# 解析解での結果の表示
print("解析解での計算結果")
print(f"u(0.1) = {analytical_values[1]:.4f}")
print(f"u(0.2) = {analytical_values[2]:.4f}")

# グラフの描画
plt.figure(figsize=(10, 6))
plt.plot(t_values, u_values, label='Euler Method', marker='o')
plt.plot(t_values, analytical_values, label='Analytical Solution', linestyle='--')
plt.title("Euler Method vs Analytical Solution")
plt.xlabel("t")
plt.ylabel("u(t)")

# t=0.1, t=0.2 の垂線を描画
plt.axvline(x=0.1, color='gray', linestyle='--', label='t = 0.1')
plt.axvline(x=0.2, color='gray', linestyle='--', label='t = 0.2')

# 赤丸と青丸を描画
plt.scatter([0.1, 0.2], [u_values[1], u_values[2]], color='red', zorder=5)
plt.scatter([0.1, 0.2], [analytical_values[1], analytical_values[2]], color='blue', zorder=5)

# 赤丸に値を表示
plt.text(0.1, u_values[1], f"{u_values[1]:.4f}", color='red', fontsize=10, ha='left')
plt.text(0.2, u_values[2], f"{u_values[2]:.4f}", color='red', fontsize=10, ha='left')

# 青丸に値を表示
plt.text(0.1, analytical_values[1], f"{analytical_values[1]:.4f}", color='blue', fontsize=10, ha='right')
plt.text(0.2, analytical_values[2], f"{analytical_values[2]:.4f}", color='blue', fontsize=10, ha='right')

plt.legend()
plt.grid()
plt.title("Euler Method and Analytical Solution of u' = t + u")
plt.show()
