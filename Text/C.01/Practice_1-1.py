import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定
#plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'Noto Sans CJK JP'

def simulate_exercise_model(x0, y0, years):
    """
    運動習慣の変化をシミュレーション
    
    Parameters:
    x0: 初期の運動している人数（比率）
    y0: 初期の運動していない人数（比率）
    years: シミュレーション年数
    
    Returns:
    x_values, y_values: 各年の人数の配列
    """
    x = np.zeros(years + 1)
    y = np.zeros(years + 1)
    
    # 初期値
    x[0] = x0
    y[0] = y0
    
    # 漸化式による計算
    for n in range(years):
        x[n+1] = 0.6 * x[n] + 0.2 * y[n]
        y[n+1] = 0.8 * y[n] + 0.4 * x[n]
    
    return x, y

# パラメータ設定
years = 12  # シミュレーション年数
time_points = np.arange(years + 1)

# 初期値の設定（x[0] = 1.0, 0.9, ..., 0.0）
initial_x_values = np.arange(1.0, -0.1, -0.1)  # 1.0から0.0まで0.1刻み

# カラーマップの設定
colors = plt.cm.viridis(np.linspace(0, 1, len(initial_x_values)))

# 統合グラフの作成
fig, ax = plt.subplots(figsize=(14, 10))

for i, x0 in enumerate(initial_x_values):
    y0 = 1.0 - x0
    x_values, y_values = simulate_exercise_model(x0, y0, years)
    
    # 運動している人（実線）
    ax.plot(time_points, x_values, '-', linewidth=2.5, 
            color=colors[i], alpha=0.9)
    
    # 運動していない人（破線）
    ax.plot(time_points, y_values, '--', linewidth=2.5, 
            color=colors[i], alpha=0.9)

# 平衡状態の線
ax.axhline(y=1/3, color='red', linestyle=':', linewidth=3, alpha=0.8, 
           label='平衡状態: x = 1/3')
ax.axhline(y=2/3, color='blue', linestyle=':', linewidth=3, alpha=0.8, 
           label='平衡状態: y = 2/3')

# 凡例の追加（線種の説明）
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='black', linewidth=2.5, linestyle='-', 
           label='運動している人 x[n] (実線)'),
    Line2D([0], [0], color='black', linewidth=2.5, linestyle='--', 
           label='運動していない人 y[n] (破線)'),
    Line2D([0], [0], color='red', linewidth=3, linestyle=':', alpha=0.8,
           label='平衡状態: x = 1/3'),
    Line2D([0], [0], color='blue', linewidth=3, linestyle=':', alpha=0.8,
           label='平衡状態: y = 2/3')
]

ax.set_xlabel('経過年数 n', fontsize=14)
ax.set_ylabel('比率', fontsize=14)
ax.set_title('運動習慣の変化モデル（12年間）\n初期値x[0] = 1.0〜0.0の全パターン', fontsize=16)
ax.grid(True, alpha=0.3)
ax.legend(handles=legend_elements, fontsize=12, loc='center right')
ax.set_xlim(0, years)
ax.set_ylim(0, 1.1)

# カラーバーの追加（axを指定）
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, 
                          norm=plt.Normalize(vmin=0, vmax=1))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, shrink=0.8)
cbar.set_label('初期値 x[0]', fontsize=12)

# 年数を整数で表示
ax.set_xticks(range(0, years+1, 2))

plt.tight_layout()
plt.show()

# 数値データの表示（代表例）
print("=== 漸化式 ===")
print("x[n+1] = 0.6×x[n] + 0.2×y[n]")
print("y[n+1] = 0.8×y[n] + 0.4×x[n]")
print()

print("=== 初期値による収束の違い（12年後） ===")
print("初期値x[0]\t12年後のx値\t12年後のy値")
for x0 in [1.0, 0.8, 0.5, 0.2, 0.0]:
    y0 = 1.0 - x0
    x_values, y_values = simulate_exercise_model(x0, y0, 12)
    print(f"{x0:.1f}\t\t{x_values[-1]:.3f}\t\t{y_values[-1]:.3f}")

print(f"\n=== 平衡状態（理論値） ===")
print(f"x = 1/3 = {1/3:.3f}")
print(f"y = 2/3 = {2/3:.3f}")
print("12年でほぼ平衡状態に到達します")
