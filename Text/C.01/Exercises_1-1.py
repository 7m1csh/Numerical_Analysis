# 演習問題１−１
"""
ユークリッドの互除法のアルゴリズムにしたがって、
m=85,n=60の最大公約数を求めよ。
また、このときの計算回数とmとnの値の変化を示せ。
"""

def gcd(m, n):
    i = 1
    while n != 0:
        m, n = n, m % n
        print(f"m: {m}" "\t" f"n: {n}")
        i += 1
    print(f"計算回数: {i}") 
    return m

# コンソールからの入力
while True:
    try:
        m = int(input("1つ目の自然数を入力してください: "))
        if m <= 0:
            raise ValueError("自然数は正の整数である必要があります。")
        break
    except ValueError as e:
        print(f"エラー: {e}. 正の整数を入力してください。")

while True:
    try:
        n = int(input("2つ目の自然数を入力してください: "))
        if n <= 0:
            raise ValueError("自然数は正の整数である必要があります。")
        break
    except ValueError as e:
        print(f"エラー: {e}. 正の整数を入力してください。")

result = gcd(m, n)
print(f"{m}と{n}の最大公約数は{result}です。")

