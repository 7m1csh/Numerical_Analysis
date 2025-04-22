# 演習問題 10.1.3
"""
ベクトルa1,a2,b は「演習問題10.1.1のとおり
a1 = [1, 1, 1]^t
a2 = [-1, 0, 1]^t
b  = [-1, 11/10, 3]^t

A = [a1, a2] としたとき、
A^t@A を係数行列とする連立1次方程式 A^t@A@x=b を解いて、
1次式による最小2乗近似を求める。

以上(演習問題10.1.2)を３Ｄ図示化する。
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# ベクトル定義
a1 = np.array([1, 1, 1])
a2 = np.array([-1, 0, 1])
b  = np.array([-1, 11/10, 3])
A = np.column_stack((a1, a2))

# 最小二乗解の計算
AtA = A.T @ A
Atb = A.T @ b
x = np.linalg.solve(AtA, Atb)
b_approx = A @ x
residual = b - b_approx

# プロット
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = np.zeros(3)

# ベクトルの描画
ax.quiver(*origin, *a1, color='r', label='a1 = [1, 1, 1]^t', arrow_length_ratio=0.1)
ax.quiver(*origin, *a2, color='g', label='a2 = [-1, 0, 1]^t', arrow_length_ratio=0.1)
ax.quiver(*origin, *b,  color='b', label='b (target) = [-1, 11/10, 3]^t', arrow_length_ratio=0.1)
ax.quiver(*origin, *b_approx, color='orange', label='b_approx (A @ x)', arrow_length_ratio=0.1)

# 残差ベクトル（投影誤差）
ax.quiver(*b_approx, *residual, color='gray', linestyle='dashed', label='residual')

# 範囲設定
max_val = np.max(np.abs([a1, a2, b, b_approx]))
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([0, max_val + 1])

# ラベルと凡例
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('最小二乗近似の可視化')
ax.legend()
plt.tight_layout()
plt.show()

