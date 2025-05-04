def get_last_lambda():
    while True:
        last_lambda = input("λの最終値 (0入力で終了。省略時はEnterで10, 0-20の整数): ")
        if lastlambda_str == "":
            return 10
        try:
            last_lambda = int(last_lambda_str)
            if 0 <= last_lambda <= 20:
                return last_lambda
            elif last_lambda == 0:
                return 0
            else:
                print("0から20までの整数を入力してください。")
        except ValueError:
            print("整数を入力してください。")

def get_mode():
    while True:
        mode = input("正規化の種類 ('L1ノルム正規化' または 'L2ノルム正規化', 'L1'または'L2'で入力): ")
        if mode in ["L1ノルム正規化", "L2ノルム正規化", "L1", "L2"]:
            return mode
        else:
            print("'L1ノルム正規化'、'L2ノルム正規化'、'L1'、または'L2'を入力してください。")

def get_stepsize():
    while True:
        s_str = input("λのステップ値 (正の実数): ")
        try:
            s = float(s_str)
            if s > 0:
                return s
            else:
                print("正の実数を入力してください。")
        except ValueError:
            print("実数を入力してください。")

if __name__ == "__main__":
    while True:
        last_lambda = get_last_lambda()
        if last_lambda == 0:
            print("プログラムを終了します。")
            break

        mode = get_mode()
        s = get_s()

        print("\n--- 入力されたパラメータ ---")
        print(f"グラフの個数 (n_trials): {n_trials}")
        print(f"正規化の種類 (mode): {mode}")
        print(f"乱数のシード値 (s): {s}")
        print("---")

        input("\n画面表示から復帰したらEnterキーを押してください...") # 画面表示からの復帰を想定

        # ここにグラフ表示などの処理を記述する (例としてプレースホルダー)
        contour_levels=50
        np.random.seed(s)
        print("グラフ表示処理を実行します")
        show_example(reg=mode,num_trials=n_trials)
