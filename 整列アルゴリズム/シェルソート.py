
# シェルソート

# 基本的な部分は、挿入ソートと同じである。
# 挿入ソートは「ほとんど整列されたデータに対しては高速」という特長があるものの、
#「隣り合った要素同士しか交換しない」ため、あまり整列されていないデータに対しては低速であった。
# そのため、適当な間隔をあけた飛び飛びのデータ列に対してあらかじめソートしておき、挿入ソートを適用すれば高速になると考えられる。
# この考え方を適用したのがシェルソートである。（Wikipediaより）

from random import randint

def shell_sort(data, kankaku):
    # 間隔が<1となった時を再起関数の終了条件として設定。
    if (len(data) == 1) or kankaku < 1: return data

    # enumerateで、リストの要素ごとにカウンターが付けられるので正確に指定できる。
    for counter, i in enumerate(data):
        
        # 対象要素をcounterで指定し、間隔と足し算が出来れば実行（つまり範囲内である）
        if counter + kankaku <= len(data) - 1:

            # 比較先の要素が元の要素より小さければ交換する。
            #こうして、大きい数は右の方へ移動する。
            if i - data[counter + kankaku] > 0:
                data[counter], data[counter+kankaku] = data[counter+kankaku], data[counter]
                print(data)  # シェルソートをイメージするためにここでprint。
                
    # 再起関数により間隔を縮んでいく。
    return shell_sort(data, kankaku - 1)


# ランダムでarrayを作成する案数、インターネットから索引。
def create_array(size=5,max=50):
    return [randint(0,max) for _ in range(size)]
a = create_array()

shell_sort(a, len(a)-1) # 間隔を出来るだけ大きめに設定し、正確さを高める。
