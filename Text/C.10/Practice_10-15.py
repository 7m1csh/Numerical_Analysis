# Practice 10.15 ラッソ回帰の係数変化
"""
出力されるグラフは、ラッソ回帰の正則化パラメータαを変化させたときの各特徴量
x1,x2,x3に対する係数の変化を示している。
以下の点が注目ポイント：
α=0.01：係数は3変数ともにほぼ等しく、元の線形回帰に近い状態。
α=0.1：少しスパース化が進み、一部の係数がわずかに減少。
α=1.0：明らかにx3の係数がゼロに近づき、重要でない特徴量として排除される傾向。
α=5.0：x2もゼロ近くになり、最終的にx1だけが残る。

解釈のポイント:
ラッソ回帰は 「特徴選択の効果」 があるため、α を大きくするにつれて、
相関の高い特徴量（この場合x1,x2,x3は線形に依存）が次々とゼロに押し込まれ、
一部の代表的な特徴だけが残るようになる。
この例では、x1,x2,x3が強く相関しているため、
ラッソはその中の一部（ここではx1）のみを残し、他を捨てている。
したがって、「ラッソは重複した説明力をもつ特徴量を除外しやすい」という性質が、
グラフに反映されている。
"""

# 必要なライブラリの再インポートとデータ定義
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合


# 説明変数と目的変数の設定
X = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [3, 6, 3],
    [4, 8, 4],
    [5, 10, 5]
])
y = np.array([1, 2, 3, 4, 5])

# 特徴量を標準化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 複数の alpha 値でラッソ回帰を実行
alphas = [0.01, 0.1, 1.0, 5.0]
lasso_coefs = []

for alpha in alphas:
    model = Lasso(alpha=alpha).fit(X_scaled, y)
    lasso_coefs.append(model.coef_)

lasso_coefs = np.array(lasso_coefs)

# プロット
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(lasso_coefs.shape[1]):
    ax.plot(alphas, lasso_coefs[:, i], marker='o', label=f'x{i+1}')

ax.set_xscale('log')
ax.set_xlabel('Lassoの正則化パラメータ α（対数スケール）')
ax.set_ylabel('係数の値')
ax.set_title('Lasso回帰：αの変化に伴う係数の推移')
ax.legend(title='特徴量')
ax.grid(True)
plt.tight_layout()
plt.show()

