# Practice 6.3 ラゲール多項式

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_laguerre
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# x の範囲（ラゲール多項式の定義域は [0, ∞)）
#x = np.linspace(0, 20, 400)
#x = np.linspace(0, 10, 400)
x = np.linspace(0, 5, 400)

# 最大次数
max_n = 5

# プロットの準備
plt.figure(figsize=(10, 6))

# 各次数 n のラゲール多項式 L_n(x) を描画
for n in range(max_n + 1):
    y = eval_laguerre(n, x)
    plt.plot(x, y, label=f"L_{n}(x)")

# グラフの装飾
plt.title("ラゲール多項式 $L_n(x)$", fontsize=14)
plt.xlabel("x")
plt.ylabel("$L_n(x)$")
#plt.yscale('symlog')  # 正負両側に対応した対数スケール
plt.axhline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

