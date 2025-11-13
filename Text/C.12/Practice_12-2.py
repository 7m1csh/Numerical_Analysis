# Practice 12.1 アナログNHK総合TVにおける菅平によるナイフエッジ効果の解析
"""
東京タワー（地上高333m）からのVHF帯（NHK総合：90–96MHz）のTV電波が、
長野県・菅平高原（標高約1250m）に回折して届いたという事例を
フレネルゾーン回折や**山越え回折（Knife-Edge Diffraction）**で解析。
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# パラメータ
freq = 90e6  # 90MHz
c = 3e8
wavelength = c / freq

# 地形設定
d1 = 160000  # 東京タワー〜菅平（m）
d2 = 15000   # 菅平〜受信点（m）
h_tx = 383   # 東京タワー高
h_obs = 1250  # 菅平の地形高
h_rx = 500    # 長野県受信点（仮）

# 距離設定
d_total = d1 + d2
x = np.linspace(0, d_total, 1000)

# 線形地形断面
terrain = np.piecewise(x,
    [x < d1, x == d1, x > d1],
    [lambda x: h_tx + (h_obs - h_tx) * x / d1,
     h_obs,
     lambda x: h_obs + (h_rx - h_obs) * (x - d1) / d2]
)

# 直線経路
line_of_sight = h_tx + (h_rx - h_tx) * x / d_total

# フレネルゾーン半径（第一）
d1_arr = x
d2_arr = d_total - x
r1 = np.sqrt(wavelength * d1_arr * d2_arr / (d1_arr + d2_arr))

# Knife-Edge Diffraction Parameter ν
h_clearance = h_obs - (h_tx + (h_rx - h_tx) * d1 / d_total)
nu = h_clearance * np.sqrt(2 * (d1 + d2) / (wavelength * d1 * d2))

# 回折損失（dB）近似：ITUモデル
def knife_edge_loss(nu):
    from scipy.special import erfc
    v = nu
    if v < -0.7:
        return 0
    else:
        return 6.9 + 20 * np.log10(np.sqrt((v - 0.1)**2 + 1) + v - 0.1)

loss_db = knife_edge_loss(nu)

# 描画
plt.figure(figsize=(10, 6))
plt.plot(x / 1000, terrain, label="地形断面", color='green')
plt.plot(x / 1000, line_of_sight, '--', label="直線経路（LOS）", color='gray')
plt.fill_between(x / 1000, line_of_sight - r1, line_of_sight + r1, color='skyblue', alpha=0.3, label="第1フレネルゾーン")
plt.axvline(d1 / 1000, color='red', linestyle=':', label="菅平（障害物）")
plt.title("東京→菅平→上田における第1フレネルゾーンと回折")
plt.xlabel("距離 (km)")
plt.ylabel("標高 (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Knife-Edge 回折パラメータ ν = {nu:.2f}")
print(f"推定回折損失 = {loss_db:.2f} dB")

