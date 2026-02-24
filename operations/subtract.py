from .utils import get_valid_int, get_valid_float

def subtract_interactive():
    subNum = 0.0
    operation = "subtract"
    totNum = get_valid_int("How many numbers would you like to " + operation + "? ")
    stNum = get_valid_float("Enter your starting number: ")

    for x in range(int(totNum - 1)):
        num = get_valid_float("Enter number " + str(x + 1) + ": ")
        subNum += num
    total = stNum - subNum
    return total
