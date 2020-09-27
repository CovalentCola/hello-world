# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:58:02 2020

@author: james
"""
from collections import Counter

#Opens text containing mass of characters from challenge's page source.
with open('rare characters.txt') as r:
    text = r.read()

#Counts each character in the txt file.
c = Counter(text)

#Prints the 8 'rarest' characters (i.e. least common).
#(Figured out it was 8 by trial-and-error)
#Clue is 'equality'.
print(c.most_common()[-8:])


r.close()