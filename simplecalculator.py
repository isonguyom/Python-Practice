# Simple CLI Calculator

print("Welcome to Simple CLI Calculator. This calculator can perform the following operations: [+, -, *, /, %]")
cal_is_running = True

# User runs the calculator
while cal_is_running:
    # Calculator is running
    print("Calculator is now running")
    user_operation = input("Which operation do you want to carry out?\n[+,-, *, /, %]: ")

    # Get user numbers
    try: # Try to get user numbers, if they're valid integers/floats, continue
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    
    except: # We get an error when running it
        print("Failed, invalid numbers...")
        continue 

    # Check the operation selected by the user.
    if user_operation == "+":
        # perform addition
        print(num1 + num2)

    elif user_operation == "-":
        # perform subtraction
        print(num1 - num2)

    elif user_operation == "*":
        # perform multiplication
        print(num1 * num2)

    elif user_operation == "/":
        # perform division
        print(num1 / num2)

    elif user_operation == "%":
        # perform modulation
        print(num1 % num2)

    else:
        # invalid operation
        print("You entered an invalid operation. Try again...")

    choice = input("Would you like to run another calculation. [y/n]: ")
    if choice == "y":
        pass 
    
    if choice == "n":
        cal_is_running = False 
        # This is the same thing as a break.-

print("Thanks for using the Calculator, bye bye...")