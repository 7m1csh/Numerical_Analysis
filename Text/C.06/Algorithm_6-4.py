# Algorithm 6.4 ホーナー法による多項式の値の計算

def horner(coeffs, a):
    result = 0
    for k in coeffs:
        result = result * a + k
    return result

def main():
    try:
        # 係数入力（例: 2,-6,2,-1）
        coeffs_input = input("多項式の係数を高次からカンマ区切りで入力してください（例: 2,-6,2,-1）: ")
        coeffs = [float(c.strip()) for c in coeffs_input.split(',')]

        # xの値を入力
        x_input = input("多項式に代入する変数 x の値を入力してください: ")
        x_value = float(x_input)

        # ホーナー法で計算
        result = horner(coeffs, x_value)

        print(f"多項式の値 P({x_value}) = {result}")

    except ValueError:
        print("数値の形式が正しくありません。係数や x の値を正しく入力してください。")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

# 実行
if __name__ == "__main__":
    main()

