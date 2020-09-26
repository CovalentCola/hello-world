import random


def displaycard(sourcefile, count):
    madlibtext = sourcefile.readlines()
    madlibq = random.choice(madlibtext)
    print(madlibq)
    while count < usercount:
        user_values.append(input('Player {playerno}, insert your answer here:\n'.format(playerno = str(count + 1))))
        count += 1
    print("The answers were: " , user_values)


#Query no. of users and assign initial score values.

user_scores = []
usercount = int(input('Insert number of players:\n'))
#user_scores = user_scores[:usercount]


f = open('madlibs.txt', 'r') #Opens external file containing list of game statements.

count = 0 #Base count for displaycard tally.
user_values = [] #Base list for user values to be appended to.
displaycard(f, count)
f.close() #Closes the external file.
