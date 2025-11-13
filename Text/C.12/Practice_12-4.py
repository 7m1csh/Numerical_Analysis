# Practice 12.4 ロトカ・ヴォルテラ方程式
"""
捕食者（Predator）と被食者（Prey）の関係を表す古典的な非線形常微分方程式モデル
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# パラメータ設定
alpha = 1.1   # 被食者の増殖率
beta  = 0.4   # 捕食率
delta = 0.1   # 捕食による捕食者増殖率
gamma = 0.4   # 捕食者の減少率

# 微分方程式の定義
def lotka_volterra(t, z):
    u1, u2 = z
    du1dt = alpha * u1 - beta * u1 * u2
    du2dt = delta * u1 * u2 - gamma * u2
    return [du1dt, du2dt]

# 初期条件
u10 = 10  # 被食者の初期個体数
u20 = 5   # 捕食者の初期個体数

# 時間の範囲
t_span = (0, 50)
t_eval = np.linspace(*t_span, 1000)

# 数値解法（RK45）
sol = solve_ivp(lotka_volterra, t_span, [u10, u20], t_eval=t_eval)

# 結果の描画
plt.figure(figsize=(12,5))

# 時系列プロット
plt.subplot(1,2,1)
plt.plot(sol.t, sol.y[0], label='被食者 u1(t)')
plt.plot(sol.t, sol.y[1], label='捕食者 u2(t)')
plt.xlabel('時間')
plt.ylabel('個体数')
plt.legend()
plt.title('ロトカ＝ヴォルテラ方程式：時間変化')

# 相平面プロット
plt.subplot(1,2,2)
plt.plot(sol.y[0], sol.y[1])
plt.xlabel('被食者 u1')
plt.ylabel('捕食者 u2')
plt.title('相平面（u1 vs u2）')
plt.grid(True)

plt.tight_layout()
plt.show()

