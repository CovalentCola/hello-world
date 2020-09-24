import math
# 10進数を2,8,16進数に変換する
#x = int(input('変換する数値をご記入ください\n'))
#print('2進数: ' + bin(x))
#print('8進数: ' + oct(x))
#print('16進数: ' +hex(x))

# 2,8,16進数を10進数に変換する
#print(int('10110', 2))
#print(int('24', 8))
#print(int('14', 16))



def twoshin(x):
    if x < 1:
        output_list.reverse()
        output_str = ""
        for i in output_list:
            output_str += i
        print(output_str.zfill(8))
        list.clear(output_list)
    elif x%2 == 0:
        output_list.append(str(0))
        twoshin(x/2)
    elif x%2 != 0:
        output_list.append(str(int(x%2)))
        twoshin(math.floor(x/2))
output_list = []

twoshin(int(input('2進数で求める10進数の数値を記入せよ(8ビットで)：\n')))
