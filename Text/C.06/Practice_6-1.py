# Practice 6.1 チェビシェフ多項式の可視化

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# チェビシェフ多項式（第1種）の定義（再帰式）
def chebyshev_T(n, x):
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return x
    else:
        T0 = np.ones_like(x)
        T1 = x
        for _ in range(2, n + 1):
            T_next = 2 * x * T1 - T0
            T0, T1 = T1, T_next
        return T1

# メイン関数
def plot_chebyshev(max_degree):
    x = np.linspace(-1, 1, 500)

    plt.figure(figsize=(10, 6))
    for n in range(max_degree + 1):
        y = chebyshev_T(n, x)
        plt.plot(x, y, label=f"T_{n}(x)")

    plt.title("チェビシェフ多項式 $T_n(x)$")
    plt.xlabel("x")
    plt.ylabel("$T_n(x)$")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# 実行部：ユーザー入力
try:
    n = int(input("描画したい最大次数 n を入力してください（例: 5）: "))
    if n < 0:
        raise ValueError("次数は0以上の整数である必要があります。")
    plot_chebyshev(n)
except ValueError as e:
    print("入力エラー:", e)

