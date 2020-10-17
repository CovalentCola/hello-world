import random
import sys

def x_randomiser():
    x = random.randrange(1, 100, 1, int)
    return x

def random_guesser ():
    global x
    user_guess = input("Input an integer between 1-100:\n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == x:
            print("Well done! The answer was indeed %d!" % x)
            rerun = input("Do you want to play again? <Y/N>\n")
            if rerun == "Y":
                x = x_randomiser()
                random_guesser()
            else:
                sys.exit()
        elif user_guess < x:
            print("No, that's too low! Try again.")
            random_guesser()
        elif user_guess > x:
            print("No, that's too high! Try again.")
            random_guesser()
        else:
            print('Try again...\n')
            random_guesser()
    else:
        print("I said an integer!\n")
        random_guesser()

x = x_randomiser()
random_guesser()

