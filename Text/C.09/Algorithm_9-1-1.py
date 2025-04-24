# Algorithm 9.1.1 べき乗法
"""
 'Algorithm 9.1 べき乗法' に途中経過を表示する機能を追加したもの。
"""

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
        print(eigenvalue)

        # 収束判定（固有値の変化が閾値以下なら停止）
        if np.linalg.norm(u - eigenvalue * y) < e:
            print(f"収束しました。収束判定値:{e}  反復回数:{_}")
            break

    return eigenvalue, y

# 行列 A と 初期ベクトル u0 の設定
A = np.array([[1, 1], [1, 0]])
u0 = np.array([1, 0])
print(f"与えられた行列 A :\n{A}\n")
print(f"与えられた初期ベクトル u0 :\n{u0}\n")

# べき乗法の適用
print("べき乗法の実行中...")
eigenvalue, eigenvector = power_method(A.copy(), u0.copy())
print()

# 結果の出力
print("べき乗法による計算結果:")
print(f"最大固有値: {eigenvalue:.6f}")
print(f"対応する固有ベクトル: {eigenvector}")
print()

# NumPyによる固有値計算
print("numpyによる計算結果：")
eigenvalue_np, eigenvector_np = np.linalg.eig(A)
print(f"最大固有値: {eigenvalue_np[0]:.6f}")
print(f"対応する固有ベクトル: {eigenvector_np[:, 0]}")

"""
実行結果：1.618034 は、フィボナッチ数列に関係する黄金比
φ= (1 + √5) / 2
に近い値であり、行列 A の最大固有値。
"""
