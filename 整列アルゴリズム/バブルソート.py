
# バブルソート・隣接交換法・交換法

# 全ての要素に関して、隣接する要素と比較し順序が逆であれば入れ替える。
# これを要素数-1回繰り返すことでソートを行なう。（Wikipediaより）

def baburu_shoujun():

    # これ以降使用するリストの初期設定。
    list_x = []

    # ユーザから数列を求める。
    x = input('整数を記入せよ。\n')

    # 数値じゃない入力値は困るので、isnumeric対策。
    if x.isnumeric():

        # 入力値をintに変換し、文字ごとにリストに保存。
        for i in x:
            list_x.append(int(i))

        # 外側のループで内側のループを繰り返す。
        count = 0
        while count < len(list_x):

            # 最大値を一番最後にずらす内側のループ。
            j = 0
            for char in list_x:

                # まずはindex out of rangeエラーにならないように設定。
                if (j + 1) == len(list_x):
                    break

                # 参照対象の数字が次の数字よりも大きければ、位置交換。
                elif list_x[j] > list_x[j + 1]:
                    list_x[j], list_x[j + 1] = list_x[j + 1], list_x[j]
                j += 1
            count += 1

        # 最後に、またstrに変換して、ユーザに出力。
        print(''.join(str(e) for e in list_x))

    else:
        exit()


baburu_shoujun()
