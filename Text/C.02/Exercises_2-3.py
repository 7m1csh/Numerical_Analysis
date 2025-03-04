# 演習問題 2.3
"""
実数 a[1],a[2],・・・,a[n] と c が与えられたとき、
以下のアルゴリズムを実行するコード。
１． k=1, m=n とする
２． もしa[k]がcより小さいときはkを１増やす
     そうでないときは、a[k]とa[m]を入れ替え、mを１減らす
３． ｋとmが一致したら終了、そうでなければステップ２に戻る
"""

def input_real_numbers():
    numbers = []
    i = 1
    while True:
        user_input = input("実数列a[n]を入力してください（a[n]の終端は何も入力せずにEnterを押してください）: ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
            print(f"a[{i}] = {number}")
            i += 1
        except ValueError:
            print("無効な入力です。実数を入力してください。")
    
    while True:
        user_input = input("実数cを入力してください : ")
        try:
            c = float(user_input)
            print(f"c = {c}")
            break
        except ValueError:
            print("無効な入力です。実数を入力してください。")
    
    return numbers, len(numbers), c


# 関数を呼び出してテスト
array, n, c = input_real_numbers()
print(f"入力された配列: {array}")
print(f"入力された数値の個数: {n}")
print(f"入力された c の値: {c}")


# 与えられた疑似コードのPythonプログラム

k = 1
m = n

while True:
    if array[k-1] < c :
        k += 1
    else:
        t = array[m-1]
        array[m-1] = array[k-1]
        array[k-1] = t
        m -= 1

    if k == m:
        break

print(f"ソート後の配列: {array}")
print(f"最終的なkの値 : {k}")

