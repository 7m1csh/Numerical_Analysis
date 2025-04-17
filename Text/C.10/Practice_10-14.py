# Practice 10.14 リッジ回帰とラッソ回帰の図式化
"""
以下の3つの回帰手法の係数（特徴量 x1, x2, x3 に対する重み）を比較:
Linear Regression（通常の回帰）：係数が自由に決まる
Ridge Regression（リッジ回帰）：大きすぎる係数を抑制（L2正則化）
Lasso Regression（ラッソ回帰）：不要な変数の係数をゼロにしやすくする（L1正則化）

結果：
通常の回帰では、x1 と強く相関する x3 にも大きな係数が与えられてしまう可能性がある（多重共線性の問題）。
Ridge では全体のバランスを取りながら小さくなっている。
Lasso では相関が強く重要度の低い x3 の係数がゼロ になる傾向が見られる。
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.preprocessing import StandardScaler
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# ダミーデータ作成（多重共線性あり）
np.random.seed(0)
n_samples = 50
X = np.random.rand(n_samples, 2)
X = np.hstack([X, X[:, [0]] + 0.01 * np.random.randn(n_samples, 1)])  # x1 と相関の高い x3 を追加
true_coef = np.array([3, -2, 0])  # x3は不要な変数と想定
y = X @ true_coef + np.random.randn(n_samples) * 0.5

# 標準化（正則化回帰に推奨される）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 回帰モデル
lin_reg = LinearRegression().fit(X_scaled, y)
ridge = Ridge(alpha=1.0).fit(X_scaled, y)
lasso = Lasso(alpha=0.1).fit(X_scaled, y)

# 係数を比較
coef_matrix = np.vstack([lin_reg.coef_, ridge.coef_, lasso.coef_])
labels = ['Linear Regression', 'Ridge Regression', 'Lasso Regression']
feature_names = ['x1', 'x2', 'x3']

# プロット
x = np.arange(len(feature_names))
width = 0.25

fig, ax = plt.subplots(figsize=(8, 6))
for i in range(coef_matrix.shape[0]):
    ax.bar(x + i * width, coef_matrix[i], width=width, label=labels[i])

ax.set_xticks(x + width)
ax.set_xticklabels(feature_names)
ax.set_ylabel('係数の値')
ax.set_title('リッジ回帰・ラッソ回帰・通常回帰の係数比較')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()

