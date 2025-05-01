# Practice 14.1 疎行列への変換 - CSR形式
"""
行列Aを入力し疎行列（CSR形式)に変換し、
行ベクトルa
列番号ベクトルc
及び列ポインターr
に格納し、出力する関数。
行列Aは、行数m、列数nの2次元リストで与えられる。
numpyは使用しないこと。
"""
import numpy as np
from scipy.sparse import csr_matrix

def sparse_matrix_to_csr(A):
    """
    疎行列をCSR形式に変換する関数
    :param A: 2次元リスト形式の行列
    :return: 行ベクトルa, 列番号ベクトルc, 列ポインターr
    """
    m = len(A)  # 行数
    n = len(A[0]) if m > 0 else 0  # 列数

    a = []  # 行ベクトル
    c = []  # 列番号ベクトル
    r = [0] * (m + 1)  # 列ポインター

    for i in range(m):
        for j in range(n):
            if A[i][j] != 0:
                a.append(A[i][j])  # 非ゼロ要素を追加
                c.append(j)  # 列番号を追加
                r[i + 1] += 1  # 行ごとの非ゼロ要素数をカウント

    for i in range(1, m + 1):
        r[i] += r[i - 1]  # 累積和を計算

    return a, c, r

# テスト
if __name__ == "__main__":
    # 行列Aの例
    A = [
        [ 5, 0, 0,-1, 0],
        [ 0, 3, 9, 0, 0],
        [ 0, 0, 1, 0, 8],
        [ 0,-2, 0, 5, 0],
        [-3, 0, 0, 2,-1]
    ]

    A_np = np.array(A)
    print(f"デモ用行列 A :\n{A_np}\n")

    a, c, r = sparse_matrix_to_csr(A)

    print("定義に基づいたロジックで変換用したCSR形式:")
    print("行ベクトルa:", a)
    print("列番号ベクトルc:", c)
    print("列ポインターr:", r)
    print()

    #numpyを使用して疎行列をCSR形式に変換
    csr = csr_matrix(A_np)
    print("numpyを使用したCSR形式:")
    print("行ベクトルa:", csr.data)
    print("列番号ベクトルc:", csr.indices)
    print("列ポインターr:", csr.indptr)

