# Practice 8.2 反復法の計算結果

import numpy as np
import matplotlib.pyplot as plt

def g(x):
    """反復関数 g(x) = cos(x)"""
    return np.cos(x)

def fixed_point_iteration(g_func, x0, max_iterations, true_solution):
    """
    不動点反復法の実行と結果表示
    
    Parameters:
    g_func: 反復関数
    x0: 初期値
    max_iterations: 最大反復回数
    true_solution: 真の解
    
    Returns:
    results: 反復結果のリスト [(x_prev, x_next), ...]
    """
    print("反復回数\t近似解\t\t\t相対誤差\t残差")
    
    results = []
    x_current = x0
    
    for n in range(max_iterations + 1):
        # 初期値以外は反復計算を実行
        if n > 0:
            x_prev = x_current
            x_current = g_func(x_prev)
            results.append((x_prev, x_current))
        
        # 統一されたprint文で出力
        relative_error = abs(x_current - true_solution) / abs(true_solution)
        residual = abs(g_func(x_current) - x_current)
        print(f"{n}\t\t{x_current:.15f}\t{relative_error:.1e}\t\t{residual:.1e}")
    
    return results

def plot_cobweb(g_func, results, x_range=(0, 1.5)):
    """
    くもの巣図の描画
    
    Parameters:
    g_func: 反復関数
    results: 反復結果のリスト
    x_range: x軸の範囲
    """
    x_vals = np.linspace(x_range[0], x_range[1], 300)
    y_vals = g_func(x_vals)

    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y_vals, label=r'$y = g(x) = \cos(x)$', color='blue', linewidth=2)
    plt.plot(x_vals, x_vals, label=r'$y = x$', color='gray', linestyle='--', linewidth=1)

    # くもの巣の軌跡を描画
    for x_old, x_new in results:
        plt.plot([x_old, x_old], [x_old, x_new], color='red', alpha=0.7, linewidth=1)  # 縦線
        plt.plot([x_old, x_new], [x_new, x_new], color='red', alpha=0.7, linewidth=1)  # 横線

    plt.title('Cobweb Plot: Fixed Point Iteration for cos(x) = x', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# 定数定義
TRUE_SOLUTION = 0.739085133215  # 高精度な不動点近似値
X0 = 0.2
MAX_ITERATIONS = 30

# メイン処理
results = fixed_point_iteration(g, X0, MAX_ITERATIONS, TRUE_SOLUTION)

# グラフ描画
plot_cobweb(g, results)

