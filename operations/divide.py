from .utils import get_valid_int, get_valid_float, check_valid_division

def divide_interactive():
    operation = "divide"
    totNum = get_valid_int("How many numbers would you like to " + operation + "? ")
    stNum = get_valid_float("Enter your starting number: ")
    curNum = stNum
    for x in range(int(totNum - 1)):
        num = get_valid_float("Enter number " + str(x + 1) + ": ")
        while not check_valid_division(num):
            num = get_valid_float("Enter number " + str(x + 1) + ": ")
        curNum /= num
        print("The current total is: " + str(curNum))
    return curNum
