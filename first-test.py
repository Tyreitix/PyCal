


def get_valid_float(prompt):
        while True:
            try:
                # Attempt to convert the input to a float
                user_input = float(input(prompt))
                # If successful, break the loop and return the float
                return user_input
            except ValueError:
                # If a ValueError is raised, print an error message and continue the loop
                print("Invalid input. Please enter a valid float.")

def get_valid_int(prompt):
        while True:
            try:
                # Attempt to convert the input to an integer
                user_input = int(input(prompt))
                # If successful, break the loop and return the integer
                return user_input
            except ValueError:
                # If a ValueError is raised, print an error message and continue the loop
                print("Invalid input. Please enter a valid integer.")

#Checks if the number entered by the user is zero for division
def check_valid_division(num):
    if num == 0:
        print("Cannot divide by zero.")
        return False
    return True

while(selection := input("Would you like to perform a calculation? (y/n) ")) == "y":
    total = 0
    selection = input("Which operation would you like to perform? \n1. add \n2. subtract  \n3. multiply  \n4. divide \n")

    match selection:
        
        #Calculates the total of the numbers entered by the user for addition
        case "1":
            operation = "add"
            totNum = get_valid_int("How many numbers would you like to " + operation + "? ")
            for x in range(int(totNum)):
                num = get_valid_float("Enter number " + str(x + 1) + ": ")
                total += num
            print("The total is: " + str(total))
        
        #Calculates the total of the numbers entered by the user for subtraction
        case "2":
            subNum = 0            
            operation = "subtract"
            totNum = get_valid_int("How many numbers would you like to " + operation + "? ")
            stNum = get_valid_float("Enter your starting number: ")

            for x in range(int(totNum - 1)):
                num = get_valid_float("Enter number " + str(x + 1) + ": ")
                subNum += num
            total = stNum - subNum
            print("The total is: " + str(total))
        
        #Calculates the total of the numbers entered by the user for multiplication
        case "3":
            operation = "multiply"
            totNum = get_valid_int("How many numbers would you like to " + operation + "? ")
            total = 1
            for x in range(int(totNum)):
                num = get_valid_float("Enter number " + str(x + 1) + ": ")
                total *= num
            print("The total is: " + str(total))
        
        #Calculates the total of the numbers entered by the user for division
        case "4":
            operation = "divide"
            totNum = get_valid_int("How many numbers would you like to " + operation + "? ")
            stNum = get_valid_float("Enter your starting number: ")
            curNum = stNum
            for x in range(int(totNum - 1)):
                num = get_valid_float("Enter number " + str(x + 1) + ": ")
                
                #Checks if the number entered by the user is zero for division
                while not check_valid_division(num):
                    num = get_valid_float("Enter number " + str(x + 1) + ": ")
                curNum /= num
                print("The current total is: " + str(curNum))
            
            print("The total is: " + str(curNum))
    
print("Goodbye!")