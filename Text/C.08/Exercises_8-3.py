# 演習問題 8.3 多変数代数方程式の解をニュートン法で求める
"""
2変数x,yについて、f(x,y)=x^2+y^2-1, g(x,y)=x^2-y とする。
xy平面上にグラフを描き、曲線の交点をしらべる。
初期値 x0=1/2, y0=1/2 としてニュートン法を１回反復して得られる近似解をもとめる。
u = f(x, y), v = g(x, y) とし、
[u, v]^t ≒  [f(x0, y0), g(x0, y0)]^t + J * [x-x0, y-y0]^t と表したときのヤコビ行列 J を求め表示する。
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

def f(x, y):
    """f(x,y) = x^2 + y^2 - 1"""
    return x**2 + y**2 - 1

def g(x, y):
    """g(x,y) = x^2 - y"""
    return x**2 - y

def F(vars):
    """ベクトル関数 F = [f, g]^T"""
    x, y = vars
    return np.array([f(x, y), g(x, y)])

def jacobian(x, y):
    """ヤコビ行列の計算
    J = [∂f/∂x  ∂f/∂y]
        [∂g/∂x  ∂g/∂y]
    """
    # f(x,y) = x^2 + y^2 - 1 の偏微分
    df_dx = 2*x
    df_dy = 2*y

    # g(x,y) = x^2 - y の偏微分
    dg_dx = 2*x
    dg_dy = -1

    return np.array([[df_dx, df_dy],
                     [dg_dx, dg_dy]])

def newton_step(x0, y0):
    """ニュートン法の1ステップ"""
    # 現在の関数値
    F_val = F([x0, y0])

    # ヤコビ行列
    J = jacobian(x0, y0)

    # ニュートン法の更新式: [x1, y1]^T = [x0, y0]^T - J^(-1) * F([x0, y0])
    delta = np.linalg.solve(J, F_val)
    x1, y1 = np.array([x0, y0]) - delta

    return x1, y1, J

# 1. グラフの描画と交点の調査
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# グラフ用のメッシュ作成
x = np.linspace(-2, 2, 400)
y = np.linspace(-1.5, 1.5, 400)
X, Y = np.meshgrid(x, y)

# 等高線（レベルセット）を描画
Z1 = f(X, Y)  # x^2 + y^2 - 1 = 0
Z2 = g(X, Y)  # x^2 - y = 0

ax1.contour(X, Y, Z1, levels=[0], colors='blue', linewidths=2, label='$x^2 + y^2 - 1 = 0$')
ax1.contour(X, Y, Z2, levels=[0], colors='red', linewidths=2, label='$x^2 - y = 0$')

# 解析的な交点を求める
# x^2 + y^2 = 1 かつ y = x^2 より
# x^2 + x^4 = 1
# x^4 + x^2 - 1 = 0
# t = x^2 とおくと t^2 + t - 1 = 0
# t = (-1 + √5)/2 (正の解のみ)
t_solution = (-1 + np.sqrt(5)) / 2
x_intersect = [np.sqrt(t_solution), -np.sqrt(t_solution)]
y_intersect = [t_solution, t_solution]

# 交点をプロット
for i, (xi, yi) in enumerate(zip(x_intersect, y_intersect)):
    ax1.plot(xi, yi, 'go', markersize=8, label=f'交点{i+1}: ({xi:.3f}, {yi:.3f})')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('曲線の交点')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_aspect('equal')

# 2. ニュートン法の1回反復
x0, y0 = 0.5, 0.5  # 初期値
x1, y1, J = newton_step(x0, y0)

print("=== ニュートン法の結果 ===")
print(f"初期値: x0 = {x0}, y0 = {y0}")
print(f"f(x0, y0) = {f(x0, y0):.6f}")
print(f"g(x0, y0) = {g(x0, y0):.6f}")
print(f"1回反復後: x1 = {x1:.6f}, y1 = {y1:.6f}")
print(f"f(x1, y1) = {f(x1, y1):.6f}")
print(f"g(x1, y1) = {g(x1, y1):.6f}")

# 3. ヤコビ行列の表示
print(f"\n=== ヤコビ行列 J(x0, y0) ===")
print(f"J = [[{J[0,0]:.1f}, {J[0,1]:.1f}],")
print(f"     [{J[1,0]:.1f}, {J[1,1]:.1f}]]")

# 右のグラフにニュートン法の反復を表示
ax2.contour(X, Y, Z1, levels=[0], colors='blue', linewidths=2, label='$x^2 + y^2 - 1 = 0$')
ax2.contour(X, Y, Z2, levels=[0], colors='red', linewidths=2, label='$x^2 - y = 0$')

# 交点をプロット
for i, (xi, yi) in enumerate(zip(x_intersect, y_intersect)):
    ax2.plot(xi, yi, 'go', markersize=8)

# 初期値と1回反復後の点をプロット
ax2.plot(x0, y0, 'ko', markersize=10, label=f'初期値: ({x0}, {y0})')
ax2.plot(x1, y1, 'ro', markersize=10, label=f'1回反復後: ({x1:.3f}, {y1:.3f})')

# 矢印で更新の様子を表示
ax2.annotate('', xy=(x1, y1), xytext=(x0, y0),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('ニュートン法の1回反復')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()

# 参考：収束まで反復した場合の結果
print(f"\n=== 参考：収束解（scipy.optimize.fsolve使用） ===")
solution = fsolve(F, [x0, y0])
print(f"収束解: x = {solution[0]:.6f}, y = {solution[1]:.6f}")
print(f"f(x, y) = {f(solution[0], solution[1]):.10f}")
print(f"g(x, y) = {g(solution[0], solution[1]):.10f}")

# 線形近似の可視化
print(f"\n=== 線形近似の説明 ===")
print("ニュートン法では、点(x0, y0)での線形近似を使用:")
print("F(x) ≈ F(x0) + J(x0) * (x - x0)")
print("この線形近似がゼロになる点を次の近似解とする:")
print("F(x0) + J(x0) * (x - x0) = 0")
print("→ x = x0 - J(x0)^(-1) * F(x0)")

