# Python-Calculator
Basic Python Calculator to do continuous Addition, Subtraction, Multiplication and Division 

Users are first met with a question "Would Would you like to perform a calculation? (y/n)". 

**If yes**

Users are met with a menu of operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division

To select an option users will input the corresponding letter(1-4)

After making their selection users are asked how many numbers/iterations of the operation they will be using. The program loops through until all iterations are complete, a grand total is displayed and resets back to main menu. 

**IF NO**

Users are met with a goodbye message signaling exiting the program. 

**Input Validation methods**
1. Ensure only integers are input for the number iterations a user will be doing
2. Float input validation to ensure users can only input float values for calculations.
3. Ensure users can only make a selection from the menu, if improper, restarts the program
4. Ensure users cannot divide by 0 during division
