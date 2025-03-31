# 固有値の条件数
"""
固有値の条件数（Eigenvalue Condition Number）とは、
行列 A の 固有値が入力の小さな摂動（変化）に対してどれほど敏感かを示す指標。
"""
import numpy as np
from scipy.linalg import eig

# 非対称行列 A
A = np.array([[1, 10**6],
              [0, 1]])

# 対称行列 B
B = np.array([[2, 1],
              [1, 2]])


# デコレータの定義
def calculate_condition_numbers(func):
    def wrapper(matrix, matrix_name):
        eigvals, cond_numbers = func(matrix)
        print(f"行列 {matrix_name} の結果:")
        for i, (eigval, cond) in enumerate(zip(eigvals, cond_numbers)):
            print(f"  固有値 {eigval:.5f} の条件数: {cond:.5f}")
        print()
    return wrapper

@calculate_condition_numbers
def compute_eigenvalue_condition_numbers(matrix):
    # 固有値と右固有ベクトル（v）を計算
    eigvals, right_vecs = eig(matrix)

    # 左固有ベクトルを求める（matrix.T の固有ベクトル）
    _, left_vecs = eig(matrix.T)

    # 条件数の計算
    cond_numbers = (
        np.linalg.norm(right_vecs, axis=0) *
        np.linalg.norm(left_vecs, axis=0) /
        (np.abs(np.einsum('ij,ij->j', right_vecs, left_vecs)) + 1e-10)
        # ゼロ除算を防ぐために、分母に非常に小さな値（例: `1e-10`）を加える
    )

    # 固有値と条件数を返す
    return eigvals, cond_numbers

print(f"条件数が大きいと思われる行列 A :\n{A}\n")
compute_eigenvalue_condition_numbers(A, "A")
print(f"条件数が小さと思われる行列 B :\n{B}\n")
compute_eigenvalue_condition_numbers(B, "B")

