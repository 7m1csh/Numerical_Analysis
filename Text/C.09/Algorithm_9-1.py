# Algorithm 9.1 べき乗法

import numpy as np

def power_method(A, u0, e=1e-6, k=1000):
    """
    べき乗法により最大固有値と固有ベクトルを求める。

    Parameters:
        A (numpy.ndarray): 正方行列 (n×n)
        u0 (numpy.ndarray): 初期ベクトル (n×1)
        e (float): 収束判定の閾値（デフォルト 1e-6）
        k (int): 最大反復回数（デフォルト 1000）

    Returns:
        eigenvalue (float): 最大固有値
        eigenvector (numpy.ndarray): 対応する固有ベクトル
    """
    u = u0 / np.linalg.norm(u0)  # 初期ベクトルを正規化

    for _ in range(k+1):
        y = u / np.linalg.norm(u)  # ベクトルを正規化
        u = np.dot(A, y)  # 行列Aをベクトルyに適用
        eigenvalue = np.dot(y.T, u)  # レイリー商で固有値を近似

        # 収束判定（固有値の変化が閾値以下なら停止）
        if np.linalg.norm(u - eigenvalue * y) < e:
            break

    return eigenvalue, y

# 行列 A と 初期ベクトル u0 の設定
A = np.array([[1, 1], [1, 0]])
u0 = np.array([1, 0])

# べき乗法の適用
eigenvalue, eigenvector = power_method(A, u0)

# 結果の出力
print(f"与えられた行列 A :\n{A}\n")
print(f"与えられた初期ベクトル u0 :\n{u0}\n")
print(f"最大固有値: {eigenvalue:.6f}")
print(f"対応する固有ベクトル: {eigenvector}")
"""
実行結果：1.618034 は、フィボナッチ数列に関係する黄金比
φ= (1 + √5) / 2
に近い値であり、行列 A の最大固有値。
"""
