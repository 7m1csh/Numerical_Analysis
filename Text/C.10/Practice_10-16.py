# Practice 10.16 リッジ回帰とラッソ回帰の係数変化
"""
Ridge回帰では全ての係数が徐々に小さくなるのに対して、
Lasso回帰では一部の係数が途中でゼロになる（スパース化）様子が観測できる。
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Lasso, Ridge
from sklearn.preprocessing import StandardScaler
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'  # Linuxの場合

# データ生成（相関のある3つの特徴量）
np.random.seed(0)
n_samples = 50
X = np.random.rand(n_samples, 1)
X = np.hstack([X, 2 * X, 3 * X])  # x1, x2=2x1, x3=3x1 のように強い相関をもたせる
y = 4 * X[:, 0] + np.random.randn(n_samples) * 0.1  # ノイズあり

# 特徴量を標準化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 各 alpha に対する係数変化の記録
alphas = [0.01, 0.1, 1.0, 5.0]
ridge_coefs = []
lasso_coefs = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    lasso = Lasso(alpha=alpha, max_iter=10000)
    ridge.fit(X_scaled, y)
    lasso.fit(X_scaled, y)
    ridge_coefs.append(ridge.coef_)
    lasso_coefs.append(lasso.coef_)

ridge_coefs = np.array(ridge_coefs)
lasso_coefs = np.array(lasso_coefs)

# 並べて可視化
fig, axs = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# Ridge回帰
for i in range(3):
    axs[0].plot(alphas, ridge_coefs[:, i], marker='o', label=f'x{i+1}')
axs[0].set_xscale('log')
axs[0].set_title('Ridge回帰の係数変化')
axs[0].set_xlabel('alpha (log scale)')
axs[0].set_ylabel('係数')
axs[0].legend()
axs[0].grid(True)

# Lasso回帰
for i in range(3):
    axs[1].plot(alphas, lasso_coefs[:, i], marker='o', label=f'x{i+1}')
axs[1].set_xscale('log')
axs[1].set_title('Lasso回帰の係数変化')
axs[1].set_xlabel('alpha (log scale)')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

