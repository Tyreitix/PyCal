def get_valid_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid float.")


def get_valid_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def check_valid_division(num):
    if num == 0:
        print("Cannot divide by zero.")
        return False
    return True
