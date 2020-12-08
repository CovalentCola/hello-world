
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

        # 入力値をintに変換し、数字ごとにリストに保存。
        for i in x:
            list_x.append(int(i))

        # エラー対策。
        if len(x) <= 0:
            exit()

        # 0番目と1番目を大小関係でソート。
        if list_x[0] > list_x[1]:
            list_x[0], list_x[1] = list_x[1], list_x[0]

        # 2文字以上であれば、挿入法本番を実行。
        if len(x) > 2:

            sounyuu_taishou = 2  # 挿入を考える値のインデックスを指す値。
            list_hikaku = 0  # 挿入対象と大小関係を比較し、適当な位置を探るための値。
            while sounyuu_taishou <= len(x)-1:  # lenは10であった場合、インデックスは9になるので1を引かなきゃ。

                # 比較位置の指定数が挿入対象の位置まで来たら挿入対象が最大ということが確定し、+1で次に進む。
                if list_hikaku == sounyuu_taishou:
                    sounyuu_taishou += 1
                    list_hikaku = 0

                # 挿入対象が比較の数より大きければ移動しないので、次の比較対象まで進めるだけ。
                elif list_x[sounyuu_taishou] >= list_x[list_hikaku]:
                    list_hikaku += 1

                # 挿入対象が比較の数より大きければ、相互交換を行う。挿入対象位置を追加し、
                elif list_x[sounyuu_taishou] < list_x[list_hikaku]:

                    # ワーク変数を利用してリストの頭に挿入対象数を入れる。
                    w = list_x[sounyuu_taishou]
                    list_x.pop(sounyuu_taishou)
                    list_x.insert(list_hikaku, w)

                    sounyuu_taishou += 1
                    list_hikaku = 0  # これ以降は新しい比較が行われるので位置をリセット。
                    print(''.join(str(e) for e in list_x))  # 挿入法のイメージを見せるため、ここでprint指定。
    else:
        exit()


sounyuuhou_shoujun()
