import random

def heap_sort(arr):
    global limit
    # The 1st max value should be at the top already so take it and move outside scan range.
    t[0], t[limit] = t[limit], t[0]
    limit -= 1 # 移動した9が範囲外となり、確定する。Reduce scan size.
    parent = 0 # 以後のループで使う変数の初期設定。ヒープの根を指す。

    # 範囲を1つずつ狭くして、整列済みの要素をlimitを超えたインデックスに退避する。
    # Lower scan range by 1 each time and place organized values outside this range.
    while limit >= 0:

        # child_parent_hikaku()をすべての要素に当てると最大値が必ず最上位に上る。
        # Using child_parent_hikaku() on all elements will force the largest
        # value to the top of the heap.
        i = limit # limitを代入し、第2のカウンターとして扱う。 Use i as a 2nd counter.
        while i >= 0:
            child_parent_hikaku(i)
            i -=  1
            
        # 新しく上がった最大値を取り出して範囲を1つ狭くする。
        # Swap new max-value with 
        t[0], t[limit] = t[limit], t[0]
        limit -= 1

    return t

# 要素交換で乱れたヒープの再構成を行う関数。
# 親と子供の値を比較し、大きいものを親の所に入れ替える。
# Swaps heap elements to rebuild the structure destroyed in previous step.
# Compares size of parent and 2 child elements, swapping largest with parent if needed.
def child_parent_hikaku(parent):
    global limit
    biggest = 0 # 最後にこの変数が親要素じゃなかったら、親と交換する。Will replace parent with this at end if needed.
    child_l = parent * 2 + 1 # Points to the index of the left child.
    child_r = parent * 2 + 2 # Points to the index of the right child.

    # ここでlimitを用いることで、確定済み要素を子として扱わないようにできる。
    # Using limit here allows us to disclude already sorted values.
    if child_l <= limit and child_r <= limit:
        
        # 両方の子要素が範囲内であった場合、大きいほうを選ぶ。
        # When both child elements are in range, picks larger one.
        if child_r <= limit:
            if t[child_l] - t[child_r] < 0:
                biggest = child_r
            else:
                biggest = child_l
                
    # 左の子要素のみが範囲内である場合。
    # In case only the left child is in range, chooses left.
    elif child_l <= limit and child_r >= limit:
        biggest = child_l # 親より大きくはないかもしれないが、次で比較するので役立つ。

    if t[biggest] < t[parent]:
        biggest = parent
                
    # 1番大きい子要素が親より大きければ親を突破し入れ替わる。
    # Switches the largest of the 3 values into position of the parent.
    elif t[biggest] > t[parent]:
        t[parent], t[biggest] = t[biggest], t[parent]


# 本プログラムに入力するランダムな配列を作成。
# Generates a random array for testing the program.
t = [51]
f=0
while f < 50:
    t.append(random.randint(1,50))
    f += 1

limit = len(t)-1 # ヒープの末尾のインデックスを指す変数。Points to tail index of heap.

print("整列前の配列：\n", t, '\n')
print("整列済みの配列：\n", heap_sort(t), '\n')
