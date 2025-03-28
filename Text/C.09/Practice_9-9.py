import numpy as np

# 対称行列 A
A = np.array([
    [4, 1, 2, 3],
    [1, 4, 3, 2],
    [2, 3, 4, 1],
    [3, 2, 1, 4]
], dtype=float)

# 1列目の2行目以降を対象に Householder 変換を作成
x = A[1:, 0]  # [1, 2, 3]
e1 = np.zeros_like(x)
e1[0] = np.linalg.norm(x) * (1 if x[0] >= 0 else -1)  # 符号を考慮
v = x - e1
v = v / np.linalg.norm(v)  # 正規化

# Householder 行列 H1 の構成（4x4サイズに拡張）
I = np.eye(4)
H1 = I.copy()
H1[1:, 1:] -= 2.0 * np.outer(v, v)

# A を変換
A1 = H1 @ A @ H1.T

print("Householder 変換行列 H1:\n", H1)
print("変換後の行列 A1:\n", A1)

print("Householder ベクトル v:", v)
print("Householder 変換行列 H1:", H1)


# A1 の 1列目（2行目以降）の要素を出力
print("A1 の 1列目（2行目以降）の要素:", A1[1:, 0])

# ゼロと見なせるか？（許容誤差を考慮してチェック）
print("ゼロと見なせるか？", np.allclose(A1[1:, 0], 0, atol=1e-10))

print("Householder ベクトル v:", v)
print("H1 @ H1.T (単位行列になれば正しい):", np.allclose(H1 @ H1.T, np.eye(H1.shape[0])))
print("A1の1列目:", A1[:, 0])

