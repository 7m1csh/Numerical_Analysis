#Algorithm 3.2 10進数小数aの2進n桁展開
"""
正の小数aが与えられたとき、配列fに小数点以下の2進ビット列を格納する
"""

def decimal_to_binary(a,n=10):
    f = []

    for _ in range(n):
        if a >= 1/2:
            f.append(1)
            a -= 1/2
        else:
            f.append(0)
 
        a *= 2

    return f


# コンソールからの入力
while True:
    r = float(input("10進の正の小数を入力してください: "))
    try:
        if (r <= 0.0) or (r >= 1.0):
            raise ValueError("正の小数である必要があります。")
        else:
            break
    except ValueError as e:
        print(f"エラー: {e}. 正の小数を入力してください。")

while True:
    try:
        n = int(input("2進小数以下の桁数を入力してください: "))
        if n <= 0:
            raise ValueError("桁数は正の整数である必要があります。")
        break
    except ValueError as e:
        print(f"エラー: {e}. 正の整数を入力してください。")

# 結果の出力
f = decimal_to_binary(r,n)
L = "".join(map(str,f))

print(f"10進数{r}の2進数展開は")
print(f"a=0.{L}")
