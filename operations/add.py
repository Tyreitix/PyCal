from .utils import get_valid_int, get_valid_float

def add_interactive():
    total = 0.0
    operation = "add"
    totNum = get_valid_int("How many numbers would you like to " + operation + "? ")
    for x in range(int(totNum)):
        num = get_valid_float("Enter number " + str(x + 1) + ": ")
        total += num
    return total
