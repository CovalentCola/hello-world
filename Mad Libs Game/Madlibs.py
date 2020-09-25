import random

f = open('madlibs.txt', 'r')

def displaycard(sourcefile):
    count = 0
    madlibtext = sourcefile.readlines()
    madlib = random.choice(madlibtext)
    print(madlib)
    user_values = []
    user_values.append(input('Enter first answer:\n'))
    user_values.append(input('Enter second answer:\n'))
    user_values.append(input('Enter third answer:\n'))
    user_values.append(input('Enter fourth answer:\n'))
    user_values.append(input('Enter final answer:\n'))
    print("The answers were: " , user_values)


displaycard(f)
f.close()
