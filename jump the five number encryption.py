
newdict = {
    "0" : "5",
    "1" : "9",
    "2" : "8",
    "3" : "7",
    "4" : "6",
    "5" : "0",
    "6" : "4",
    "7" : "3",
    "8" : "2",
    "9" : "1"
    }


def dictcheck(inputstring):
    if inputstring == "":
        print("error: the following arguments are required: str")
        dictcheck(str(input("Input a string of numbers:\n")))
    else:
        print(inputstring.translate(str.maketrans(newdict)))

dictcheck(str(input("Input a string of numbers:\n")))
