# 演習問題 10.4
"""
ベクトルa1,a2,a3,及びvを以下のように定義する。
a1 = [2, 1]^t
a2 = [1, 2]^t
a3 = [-1, 1]^t
v = [-1, 3]^t
各ベクトルを2次元座標に図示せよ。
ベクトルｖとベクトルa1,a2,及びa3がなす角θ1,2,3と
cosθ1,cosθ2,cosθ3を図の中に表示せよ。
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# ベクトル定義
a1 = np.array([2, 1])
a2 = np.array([1, 2])
a3 = np.array([-1, 1])
v = np.array([-1, 3])

# 単位ベクトルとcosθの計算
def cosine_angle(u, v):
    cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    theta_deg = np.degrees(np.arccos(cos_theta))
    return theta_deg, cos_theta

theta1, cos1 = cosine_angle(a1, v)
theta2, cos2 = cosine_angle(a2, v)
theta3, cos3 = cosine_angle(a3, v)

# 角度とcosθの計算結果を表示
print(f"θ1 = {theta1:.2f}°, cosθ1 = {cos1:.3f}")
print(f"θ2 = {theta2:.2f}°, cosθ2 = {cos2:.3f}")
print(f"θ3 = {theta3:.2f}°, cosθ3 = {cos3:.3f}")

print(f"1/(5*√2) = {1/(5*np.sqrt(2)):.3f}")
print(f"1/√2 = {1/np.sqrt(2):.3f}")
print(f"2/√5 = {2/np.sqrt(5):.3f}")

# プロット
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2.5, 3)
ax.set_ylim(-1, 4)
ax.grid(True)
ax.set_aspect('equal')

# ベクトル描画
def draw_vector(v, color, label):
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

draw_vector(a1, 'blue', 'a1')
draw_vector(a2, 'green', 'a2')
draw_vector(a3, 'purple', 'a3')
draw_vector(v, 'red', 'v')

# 角度とcosθのテキスト表示
ax.text(0.5, 3.5, f'θ1 = {theta1:.2f}°, cosθ1 = {cos1:.3f}', color='blue')
ax.text(0.5, 3.2, f'θ2 = {theta2:.2f}°, cosθ2 = {cos2:.3f}', color='green')
ax.text(0.5, 2.9, f'θ3 = {theta3:.2f}°, cosθ3 = {cos3:.3f}', color='purple')

ax.legend()
plt.title("Vectors and Angles with v")
plt.show()

