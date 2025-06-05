# Practice 7.5 ルンゲの現象の可視化

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator


from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# Runge関数の定義
def runge(x):
    return 1 / (1 + 25 * x**2)

# 実験：補間点数 n を変えて比較（例：5, 10, 15）
degrees = [5, 10, 15]

# プロット用の細かいx値
x_dense = np.linspace(-1, 1, 1000)
y_true = runge(x_dense)

# プロットの準備
plt.figure(figsize=(10, 6))

for n in degrees:
    # 等間隔の補間点
    x_nodes = np.linspace(-1, 1, n + 1)
    y_nodes = runge(x_nodes)

    # ラグランジュ補間（Barycentricは数値的に安定）
    interpolator = BarycentricInterpolator(x_nodes, y_nodes)
    y_interp = interpolator(x_dense)

    # 描画
    plt.plot(x_dense, y_interp, label=f"補間次数 n={n}")
    plt.plot(x_nodes, y_nodes, 'o', color='black')  # 補間点のプロット

# 元の関数の描画
plt.plot(x_dense, y_true, 'k--', label="Runge関数 f(x)", linewidth=2)

plt.title("ルンゲの現象の可視化（等間隔点による多項式補間）")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.ylim(-0.5, 2.5)
plt.show()

