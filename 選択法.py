
# 選択法

# データ列中で一番小さい値を探し、1番目の要素と交換する。
# 次に、2番目以降のデータ列から一番小さい値を探し、2番目の要素と交換する。
# これを、データ列の最後まで繰り返す

def sentakuhou():
    # これ以降使用するリストの初期設定。
    list_x = []
    return_list = []

    # ユーザから数列を求める。
    x = input('整数を記入せよ。\n')
    # 数値じゃない入力があったら困るので、対策。
    if x.isnumeric():
        # 入力値をintに変換し、リストに保存。
        for i in x:
            list_x.append(int(i))

        length_seigen = len(list_x)  # 後で指定したら常に変化していたのでここにて初期設定。
        j = 0  # 次ループのカウンター用。
        while j < length_seigen:
            return_list.append(min(list_x))  # 最低値を出力リストに追加。
            list_x.pop(list_x.index(min(list_x)))  # 取り出した値を元リストから削除。
            j += 1
        return return_list
    else:
        exit()
