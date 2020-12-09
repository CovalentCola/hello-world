
# クイックソート

# 整列の特定な値を軸として扱い、軸より大きい数を一つのグループにわけ、
# 軸より小さい数をもう一つのグループに分ける。最後に、軸と同じ値の数を
# 3つ目のグループに分ける。グループを合わせて整列が完成する。

import math


def quicksort(data_list):

    # 後述の再起関数の終了条件を設定。
    if len(data_list) <= 1:
        return data_list

    # 基準値との大小関係により、グループを初期設定。
    smaller_group, equal_group, larger_group = [], [], []

    # 数列の中央値を軸とする。こちらは入力されたリストのインデックスを指定する。
    pivot = data_list[math.ceil((len(data_list)) / 2) - 1]

    # 軸との大小関係により、実際に数を分けていく。
    for i in data_list:
        if i < pivot:
            smaller_group.append(i)
        elif i == pivot:
            equal_group.append(i)
        else:
            larger_group.append(i)

    # 再起関数。分けておいたグループを更に分けて小さくする。こうして、小さい値から昇順に出力される。
    return quicksort(smaller_group) + equal_group + quicksort(larger_group)


# 入力値を保管するリストの初期設定。
list_x = []

# 整列を行うために、ユーザから数列を求める。
x = input('整数を記入せよ。\n')

# 数値じゃない入力値は困るので、isnumeric対策。
if x.isnumeric():

    # 入力値をintに変換し、数字ごとにリストに保存。
    for val in x:
        list_x.append(int(val))

    # 関数を呼んで、返ってきたリストを元通りストリングに変換、出力。
    print(''.join(str(e) for e in quicksort(list_x)))

# エラー対策。
else:
    print('整数のみ入力してください。')
    exit()
