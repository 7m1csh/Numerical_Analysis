# 演習問題 2.2
"""
相異なるｎ個の実数a[n],a[2],・・・,a[n]が与えられたとき、
昇順にソーティングするアルゴリズム。
"""

def input_real_numbers():
    numbers = []
    while True:
        user_input = input("実数を入力してください（終了する場合は何も入力せずにEnterを押してください）: ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("無効な入力です。実数を入力してください。")
    
    return numbers, len(numbers)

# 関数を呼び出してテスト
array, n = input_real_numbers()
print(f"入力された配列: {array}")
print(f"入力された数値の個数: {n}")


# 与えられた疑似コードのPythonプログラム

for i in range(1, n-1):
    if array[i+1] < array[i]:
        t = array[i+1]
        array[i+1] = array[i]
        array[i] = t
        print(f"forループ {i} 回目: {array}")

print(f"ソート後の配列: {array}")

