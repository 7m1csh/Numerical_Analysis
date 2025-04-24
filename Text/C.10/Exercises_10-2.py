# 演習問題 10.2
"""
ベクトルa1,a2,b は「演習問題10.1.1のとおり
a1 = [1, 1, 1]^t
a2 = [-1, 0, 1]^t
b  = [-1, 11/10, 3]^t

A = [a1, a2] としたとき、
Aをハウスホルダー変換する。
Aの列ベクトルa1の対角要素より下を0とする
ハウスホルダー行列の法線ベクトルuを求める
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# ベクトル定義
"""
a1 = np.array([1, 1, 1])
a2 = np.array([-1, 0, 1])
b  = np.array([-1, 11/10, 3])
A = np.column_stack((a1, a2))
"""

# 列ベクトル a1 の定義
a1 = np.array([1, 1, 1], dtype=float)
print(f"ベクトル v: {a1}\n")

# 対角要素以下を0にしたい ⇒ 先頭要素以外を0とするベクトル e1
e1 = np.zeros_like(a1)
e1[0] = -np.linalg.norm(a1)

#対角要素以下を0にしたベクトルe1の表示
print("対角要素以下を0にしたベクトル w: w(0) = ||v||")
print(e1)
print()

# ハウスホルダーの反射ベクトル u
u = a1 - e1
print("反射ベクトル: v - w")
print(u)
print()
print("反射ベクトルのノルム: ||v - w||")
nu = np.linalg.norm(u)
print(f"{nu}\n")

#u = u / np.linalg.norm(u)  # 正規化
u = np.sqrt(2) * u / nu

# 結果表示
print("法線ベクトル u: √2 * (v - w) / ||v - w||")
print(u)

print(f"\nα = √2 / √(2 + (1 + √3)**2) = {(np.sqrt(2) / np.sqrt(2 + (1 + np.sqrt(3))**2))}")
print(f"β = √2 * (1 + √3) / √(2 + (1 + √3)**2) = {np.sqrt(2) * (1 + np.sqrt(3)) / np.sqrt(2 + (1 + np.sqrt(3))**2)}")

# プロット準備
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 原点
origin = np.zeros(3)

# ベクトル描画
ax.quiver(*origin, *a1, color='blue', label='v', arrow_length_ratio=0.1)
ax.quiver(*origin, *e1, color='green', label='w (target)', arrow_length_ratio=0.1)
ax.quiver(*origin, *u, color='red', label='u (normal vector)', arrow_length_ratio=0.1)

# u に垂直な平面（鏡面）の描画
# 平面上の格子点を作成
xx, yy = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10))

# 法線ベクトル u = [a, b, c] を使って平面の方程式 a*x + b*y + c*z = 0 を解く
a, b, c = u
# z = (-a*x - b*y)/c
zz = (-a * xx - b * yy) / c

# 平面を描画（alpha=0.3 で半透明）
#ax.plot_surface(xx, yy, zz, color='red', alpha=0.3, label='mirror plane')
ax.plot_surface(xx, yy, zz, color='red', alpha=0.3)

# 軸設定
max_range = 2
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("ハウスホルダー法：法線と鏡面の可視化")
ax.legend()
plt.tight_layout()
plt.show()
