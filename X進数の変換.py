import math
import time


# 10進数から2進数に変換する関数。
def twoshin(x):
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
        twoshin(x/2) # 割り切った偶数をまた関数に通す。
    elif x%2 != 0:
        two_output_list.append('1') # 奇数の場合、そのまま結果リストに1を追加
        twoshin(math.floor(x/2)) # xを2で割った結果を切り捨て、関数に再度通す。
    else:
        print('エラーが発生しました。終わります。') # 起こらないはずだが、一応。
        time.sleep(2)
        sys.exit()
two_output_list = []

# 2進数から10進数に変換する関数。
def tenshin():
    allowed_chars = set('01') # 「1」と「0」のみが入力できるようにセットする。
    y = input('10進数で求める2進数の数値を記入せよ：\n')
    if y and allowed_chars.issuperset(y): # 「1」「0」以外がなければ進む。
            str_y = str(y) # 順番に追加できるためにストリング変換。
            z = len(str_y) - 1 # ストリングの長さで、個々の数字の重さが全てわかる。
            power = 0
            tenshin_output = []
            while z >= 0: # 位置を順番に計算し、インプットの長さである「ｚ」を減らしていく。
                tenshin_output.append(str(int(str_y[z]) * (2 ** power))) # 位置ごとの重さを計算しアウトプットに追加。
                power +=1
                z -= 1
            tenshin_output = list(map(int, tenshin_output)) # リストの数値はストリングなので整数に変換。
            print(sum(tenshin_output)) # 計算した数値を合わせて、結果として出す。
    else:
        print('「1」と「0」しか入力できません。もう1度確認してください。')
        time.sleep(1)
        tenshin()

# ユーザーに選択肢を挙げる。回答によって2進数か10進数への変換関数を起動させる。
def convert_choice(): 
    choice = input('どの変換をお求めですか。\n <1>=10進数→2進数、<2>=2進数→10進数。\n')
    if choice == '1':
        twoshin_input = input('2数で求める10進数の数値を記入せよ：\n')
        if twoshin_input.isnumeric():
            twoshin(int(twoshin_input))
        else:
            print('数字しか入力できません。最初に戻ります。')
            time.sleep(1)
    elif choice == '2':
        tenshin()
    else:
        print("\n「１」か「２」をのみ入力してください。\n")
        time.sleep(1)
        convert_choice()
    
convert_choice()
