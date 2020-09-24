import random

x = random.randrange(1, 100, 1, int)


def random_guesser (x):
    user_guess = int(input("Input an integer between 1-100:\n"))
    if user_guess == x:
        print("Well done! The answer was indeed %d!" % x)
        input("Please rerun the script to play again.\n")
    elif user_guess < x:
        print("No, that's too low! Try again.")
        random_guesser(x)
    elif user_guess > x:
        print("No, that's too high! Try again.")
        random_guesser(x)

random_guesser(x)

