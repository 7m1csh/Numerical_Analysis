# Algorithm 6.5 多項式の高階導関数値の計算

import math

def extended_horner(coeffs, alpha, m):
    """
    多項式のk次導関数をホーナー法で評価（0次～m次）
    返り値: beta_list[k] = f^{(k)}(alpha) / k!
    """
    a = coeffs.copy()
    n = len(a)
    if m >= n:
        raise ValueError(f"導関数の最高階 m = {m} は、多項式の次数 {n - 1} 以下である必要があります。")

    # beta_list[k] = f^{(k)}(alpha) / k!
    beta = [0.0 for _ in range(m + 1)]
    work = [0.0 for _ in range(m + 1)]

    beta[0] = a[0]

    for k in range(1, n):
        work[0] = beta[0]
        beta[0] = beta[0] * alpha + a[k]
        for j in range(1, min(k + 1, m + 1)):
            work[j] = beta[j]
            beta[j] = beta[j] * alpha + work[j - 1]
            #print(f"k={k}, j={j}, beta(j)={beta[j]}")
    return beta


def main():
    try:
        # 係数入力
        coeffs_input = input("多項式 f(x) の係数を高次からカンマ区切りで入力してください（例: 1,-3,2）: ")
        coeffs = [float(c.strip()) for c in coeffs_input.split(',')]
        degree = len(coeffs) - 1

        # x = alpha の入力
        alpha_input = input("多項式に代入する変数 x = α の値を入力してください: ")
        alpha = float(alpha_input)

        # m の入力
        m_input = input("求めたい導関数の最高階 m を入力してください（例: 2）: ")
        m = int(m_input)

        # 妥当性チェック
        if m < 0:
            raise ValueError("m は 0 以上の整数でなければなりません。")
        if m > degree:
            raise ValueError(f"m = {m} は多項式の次数 {degree} を超えています。")

        # 拡張ホーナー法による計算
        beta_list = extended_horner(coeffs, alpha, m)

        # 出力
        print(f"\n--- beta(k) = f^{{(k)}}(α) / k! の出力 ---")
        for k in range(m + 1):
            print(f"beta({k}) = {beta_list[k]}")

    except ValueError as ve:
        print(f"⚠️ 入力エラー: {ve}")
    except Exception as e:
        print(f"⚠️ 予期しないエラーが発生しました: {e}")

# 実行
if __name__ == "__main__":
    main()

