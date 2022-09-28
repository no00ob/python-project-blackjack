# Not included in main program this is for testing specific methods and functions

import strings

faceCards = [11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52]
aceCards = [1, 14, 27, 40]

def IntToCard(var):
    if (var >= 2 and var <= 10):
        var = var
    elif (var >= 15 and var <= 23):
        var = var - 13
    elif (var >= 28 and var <= 36):
        var = var - 13 * 2
    elif (var >= 41 and var <= 49):
        var = var - 13 * 3
    elif (faceCards.__contains__(var)):
        var = 10
    elif (aceCards.__contains__(var)):
        var = 1
    else:
        var = 2
        raise Exception(strings.integerException)
    return var

print(IntToCard(int(input("Input card "))))