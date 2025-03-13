#Algorithm 3.1 10進数から2進数への変換
"""
正の整数aが与えられたとき、配列kに2進ビット列を格納する
"""

def decimal_to_binary(a):
    i = 0
    k = []
    while a > 0:
        k.append(a % 2)
        a = a // 2
        i += 1
    return k


# コンソールからの入力
while True:
    try:
        n = int(input("10進の正の整数を入力してください: "))
        if n <= 0:
            raise ValueError("正の整数である必要があります。")
        break
    except ValueError as e:
        print(f"エラー: {e}. 正の整数を入力してください。")


# 結果の出力
k = decimal_to_binary(n)
k.reverse()
print(k)
