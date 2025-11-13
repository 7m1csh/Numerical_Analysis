# Practice 12.3 ロジスティック方程式
"""
初期は指数関数的に増加。
やがて成長は鈍化し、xはKに収束。
資源が有限である現実世界の増殖モデル。
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# パラメータ
mu = 0.3      # 成長率
K = 1000     # 環境収容力
n0 = 10      # 初期個体数

# 解析解
def logistic(t):
    return K / (1 + ((K - n0) / n0) * np.exp(-mu * t))

# 描画
t = np.linspace(0, 50, 500)
n = logistic(t)

plt.plot(t, n, label='n(t)')
plt.axhline(K, color='gray', linestyle='--', label='K（環境収容力）')
plt.xlabel('時間 t')
plt.ylabel('個体数 n(t)')
plt.title('ロジスティック方程式の解')
plt.legend()
plt.grid(True)
plt.show()

