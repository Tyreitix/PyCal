from .utils import get_valid_int, get_valid_float

def multiply_interactive():
    operation = "multiply"
    totNum = get_valid_int("How many numbers would you like to " + operation + "? ")
    total = 1.0
    for x in range(int(totNum)):
        num = get_valid_float("Enter number " + str(x + 1) + ": ")
        total *= num
    return total
