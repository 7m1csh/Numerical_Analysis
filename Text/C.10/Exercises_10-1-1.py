# 演習問題 10.1.1
"""
以下のベクトルを図示せよ。
a1 = [1, 1, 1]^t
a2 = [-1, 0, 1]^t
b  = [-1, 11/10, 3]^t
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# ベクトルの定義
a1 = np.array([1, 1, 1])
a2 = np.array([-1, 0, 1])
b  = np.array([-1, 11/10, 3])

# 原点
origin = np.zeros(3)

# 3D プロットの準備
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ベクトルの描画
ax.quiver(*origin, *a1, color='r', label='a1=[1, 1, 1]^t', arrow_length_ratio=0.1)
ax.quiver(*origin, *a2, color='g', label='a2=[-1, 0, 1]^t', arrow_length_ratio=0.1)
ax.quiver(*origin, *b,  color='b', label='b=[-1, 11/10, 3]^t',  arrow_length_ratio=0.1)

# 軸範囲設定
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([0, 4])

# 軸ラベル
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 凡例表示
ax.legend()
ax.set_title("3Dベクトルの可視化")

plt.tight_layout()
plt.show()

