# Practice 6.2 ルジャンドル多項式

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# x の値を定義（-1 から 1 の範囲）
x = np.linspace(-1, 1, 400)

# 描画する最大次数
max_n = 5

# プロットの準備
plt.figure(figsize=(10, 6))

# 各次数のルジャンドル多項式を計算・描画
for n in range(max_n + 1):
    Pn = legendre(n)  # scipyのlegendre関数は次数nのルジャンドル多項式を返す
    y = Pn(x)
    plt.plot(x, y, label=f"P_{n}(x)")

# グラフの設定
plt.title("ルジャンドル多項式 $P_n(x)$", fontsize=14)
plt.xlabel("x")
plt.ylabel("$P_n(x)$")
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

