
# 挿入法

# まず0番目と1番目の要素を比較し、順番が逆であれば入れ換える。
# 次に、2番目の要素が1番目までの要素より小さい場合、正しい順に並ぶように「挿入」する（配列の場合、前の要素を後ろに一つずつずらす）。
# この操作で、2番目までのデータが整列済みとなる（ただし、さらにデータが挿入される可能性があるので確定ではない）。
# このあと、3番目以降の要素について、整列済みデータとの比較と適切な位置への挿入を繰り返す。 （Wikipediaより）

def sounyuuhou_shoujun():

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


sounyuuhou_shoujun()
