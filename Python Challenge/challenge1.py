"""
Created on Sun Sep 27 15:16:16 2020

@author: james
"""

'''
#http://www.pythonchallenge.com/pc/def/map.html

#This was my first attempt w/o using maketrans() and translate().
def stringmorpher(str):
    for i in range(len(str)):
        if str[i] == 'y':
            str[i] = 'a'
        elif str[i] == 'z':
            str[i] = 'b'
        elif str[i] != '.' and str[i] != ' ' and str[i] != '(' and str[i] != ')' and str[i] != "'":
            str[i] = chr(ord(str[i])+2)
    print(' '.join(str))
'''

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "http://www.pythonchallenge.com/pc/def/map.html"

#Using maketranslate() and translate() to convert the string is much easier.
maptable = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')

print(text.translate(maptable))
print(url.translate(maptable)) #'ocr' for next clue.
