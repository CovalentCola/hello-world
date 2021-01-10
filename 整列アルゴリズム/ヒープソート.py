import random

def heap_sort(arr):
    global limit
    t[0], t[limit] = t[limit], t[0]
    limit -= 1 # 移動した9が範囲外となり、確定する。
    parent = 0 # 以後のループで使う変数の初期設定。ヒープの根を指す。

    # 範囲を1つずつ狭くして、整列済みの要素をlimitを超えたインデックスに退避する。
    while limit >= 0:

        # child_parent_hikaku()をすべての要素に当てると最大値が必ず最上位に上る。
        i = limit # limitを代入し、第2のカウンターとして扱う。
        while i >= 0:
            child_parent_hikaku(i)
            i -=  1
            
        # 新しく上がった最大値を取り出して範囲を1つ狭くする。
        t[0], t[limit] = t[limit], t[0]
        limit -= 1

    return t

# 要素交換で乱れたヒープの再構成を行う関数。
# 親と子供の値を比較し、大きいものを親の所に入れ替える。
def child_parent_hikaku(parent):
    global limit
    biggest = 0 # 最後にこの変数が親要素じゃなかったら、親と交換する。
    child_l = parent * 2 + 1
    child_r = parent * 2 + 2

    # ここでlimitを用いることで、確定済み要素を子として扱わないようにできる。
    if child_l <= limit and child_r <= limit:
        
        # 両方の子要素が範囲内であった場合、大きいほうを選ぶ。
        if child_r <= limit:
            if t[child_l] - t[child_r] < 0:
                biggest = child_r
            else:
                biggest = child_l
                
        # 左の子要素のみが範囲内である場合。
    elif child_l <= limit and child_r >= limit:
        biggest = child_l # 親より大きくはないかもしれないが、次で比較するので役立つ。

    if t[biggest] < t[parent]:
        biggest = parent
                
    # 1番大きい子要素が親より大きければ親を突破し入れ替わる。
    elif t[biggest] > t[parent]:
        t[parent], t[biggest] = t[biggest], t[parent]


# 本プログラムに入力するランダムな配列を作成。
t = [51]
f=0
while f < 50:
    t.append(random.randint(1,50))
    f += 1
limit = len(t)-1 # ヒープの末尾のインデックスを指す変数。

print("整列前の配列：\n", t, '\n')
print("整列済みの配列：\n", heap_sort(t), '\n')
