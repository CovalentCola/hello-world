import math
import time
import sys

# 10進数から2進数に変換する関数。
def tentwoshin(x):
    global two_output_list # 定義外の変数にアクセス。
    if x < 1:
        two_output_list.reverse() # 紙で解くと同じく、結果を逆順番にする。
        output_str = ""
        for i in two_output_list: # 結果リストを綺麗なストリングに変更。
            output_str += i
        print(output_str.zfill(8)) # 8ビットにするため、必ず8文字になる。足りなければ0で満たす。
        list.clear(two_output_list) # 繰り返し出来るよう、リストを空に戻す。
    elif x%2 == 0:
        two_output_list.append(str(0)) # 偶数の場合、そのまま結果リストに0を追加。
        tentwoshin(x/2) # 割り切った偶数をまた関数に通す。
    elif x%2 != 0:
        two_output_list.append('1') # 奇数の場合、そのまま結果リストに1を追加
        tentwoshin(math.floor(x/2)) # xを2で割った結果を切り捨て、関数に再度通す。
    else:
        print('エラーが発生しました。終わります。') # 起こらないはずだが、一応。
        time.sleep(1.5)
        sys.exit()
two_output_list = [] # why here???



# 2進数から10進数に変換する関数を定義。
def twotenshin():
    # 入力には「1」「0」「.」の文字のみを許可する設定。
    allowed_chars = set('01.')
    
    y = input('10進数で求める2進数の数値を記入せよ：\n')

    # 許可された文字だけ入力されていれば実行する。
    if y and allowed_chars.issuperset(y):

        # いくつかの変数を定義しておく。
        decpointcount = 0
        decpointlocation = 0
        valuelocations = []
        locationweights = []
        
        # 小数点が一つだけ入力されたかを確認。
        for i in y:
            if i == '.': 
                decpointcount = decpointcount + 1
        
        if decpointcount > 1: # 小数点が２つ以上見つかった場合、プログラムを停止する。
            print("エラー：「.」が一個以上発見されました。最初に戻ります。\n")
            time.sleep(1.5)
            twotenshin()
            # 理想的ではないが、ここでプログラム停止命令をしなければ様子がおかしくなる。
            sys.exit()
            
        elif decpointcount == 1: # 小数点が１つだけ見つかった場合、位置を特定する。
            decpointlocation = y.find(".")
            
        elif decpointcount == 0: # 小数点が見つからなかった場合、入力された値の末尾にあると宣言する。
            decpointlocation = len(y)
        
        # それぞれの「１」の重さを計るために、位置を特定し、貯蔵する。
        for n in range(len(y)):
            if y[n] == '1':
                valuelocations.append(n)
        
        # それぞれの「１」と小数点の位置を比較し、重さを計る。
        for i in valuelocations:
            if i < decpointlocation:
                locationweights.append( 2**((decpointlocation-i)-1) )
            elif i > decpointlocation:
                locationweights.append( 2**-(i - decpointlocation) )

        # 価値のある値は「１」だけなので、そのまま合計を返せば終わり。
        answer = sum(locationweights)
        print(f"２進数の「{y}」を１０進数で表すと「{answer}」になる。\n")

    # 違法な文字が入力された場合、再度入力を求める。
    else:
        print('「1」「0」「.」しか入力できません。もう1度確認してください。\n')
        time.sleep(1.5)
        twotenshin()



# ユーザーに選択肢を挙げる。回答によって2進数か10進数への変換関数を起動させる。
def convert_choice(): 
    choice = input('どの変換をお求めですか。\n <1>=10進数→2進数、<2>=2進数→10進数。\n')
    if choice == '1':
        tentwoshin_input = input('2進数で求める10進数の数値を記入せよ：\n')
        if tentwoshin_input.isnumeric():
            tentwoshin(int(tentwoshin_input))
        else:
            print('数字しか入力できません。最初に戻ります。\n')
            time.sleep(1)
            convert_choice()
    elif choice == '2':
        twotenshin()
    else:
        print("\n「１」か「２」をのみ入力してください。\n")
        time.sleep(1)
        convert_choice()
    
convert_choice()
