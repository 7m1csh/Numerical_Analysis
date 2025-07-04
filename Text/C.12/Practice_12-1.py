import numpy as np
import matplotlib.pyplot as plt

# パラメータ
freq = 2.4e9  # 周波数 2.4GHz（Wi-Fi帯）
c = 3e8       # 光速
wavelength = c / freq  # 波長 λ
d_total = 100.0  # A-B間距離（メートル）
n = 1  # 第nフレネルゾーン

# 点AとBの座標
A = np.array([0, 0])
B = np.array([d_total, 0])

# 可視化用座標格子
x = np.linspace(0, d_total, 500)
z = np.linspace(-20, 20, 400)
X, Z = np.meshgrid(x, z)

# 各点における距離 d1（Aから）、d2（Bまで）
d1 = np.sqrt((X - A[0])**2 + Z**2)
d2 = np.sqrt((X - B[0])**2 + Z**2)

# フレネル半径 r_n
rn = np.sqrt(n * wavelength * d1 * d2 / (d1 + d2))

# フレネルゾーンの内部を描く（rn >= r → 内部）
inside = d1 + d2 - (np.linalg.norm(B - A)) <= wavelength / 2

# 描画
plt.figure(figsize=(10, 6))
plt.contourf(X, Z, d1 + d2 - (np.linalg.norm(B - A)) < wavelength / 2, levels=[0.5, 1], colors=['#66ccff'])
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label='Line of Sight')
plt.scatter([A[0], B[0]], [A[1], B[1]], color='red', label='Tx / Rx')
plt.title(f'1st Fresnel Zone at {freq/1e9:.1f} GHz (λ = {wavelength:.2f} m)')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

