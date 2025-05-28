# Practice 6.4 物理系エルミート多項式

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite  # 物理系エルミート多項式
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# xの範囲と点の生成
x = np.linspace(-4, 4, 400)

# プロットする次数の最大値
max_n = 5

# グラフ描画
plt.figure(figsize=(10, 6))
for n in range(max_n + 1):
    y = eval_hermite(n, x)
    plt.plot(x, y, label=f'$H_{{{n}}}(x)$')

plt.title('エルミート多項式 $H_n(x)$', fontsize=14)
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$H_n(x)$', fontsize=12)
plt.ylim(-100, 100)  # y軸の範囲を制限して振動部分を見やすく
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

