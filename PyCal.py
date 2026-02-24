from operations import (
    add_interactive,
    subtract_interactive,
    multiply_interactive,
    divide_interactive,
)


def main():
    while (selection := input("Would you like to perform a calculation? (y/n) ")) == "y":
        selection = input(
            "Which operation would you like to perform? \n1. add \n2. subtract  \n3. multiply  \n4. divide \n"
        )

        match selection:
            case "1":
                total = add_interactive()
                print("The total is: " + str(total))

            case "2":
                total = subtract_interactive()
                print("The total is: " + str(total))

            case "3":
                total = multiply_interactive()
                print("The total is: " + str(total))

            case "4":
                total = divide_interactive()
                print("The total is: " + str(total))


    print("Goodbye!")


if __name__ == "__main__":
    main()