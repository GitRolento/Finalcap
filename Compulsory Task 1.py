import os

#Function that performs the arithmetic operation based on the users input.
def perform_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == 'x':
        return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Cannot divide by zero."
    else:
        return "Invalid operator. Please use +, -, x, or /."

#This function writes the calculation result to a file named "calculations.txt".
def write_to_file(num1, num2, operator, result):
    with open('calculations.txt', 'a') as file:
        file.write(f"{num1} {operator} {num2} = {result}\n")

#This function reads the contents of a file and returns it to the user.
def read_from_file(filename):
    if not os.path.exists(filename):
        return "File not found. Please enter a valid file name."
    with open(filename, 'r') as file:
        return file.read()

#Validate number input and return the valid integer
def get_valid_number_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return num

#This function implements the menu and overall functionality of the calculator.
def calculator():
    while True:
        print("Enter 1 to perform a calculation")
        print("Enter 2 to read from a file")
        print("Enter 3 to exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            num1 = get_valid_number_input("Enter first number: ")
            num2 = get_valid_number_input("Enter second number: ")
            operator = input("Enter operator (+, -, x, /): ")
            result = perform_operation(num1, num2, operator)
            print("Result:", result)
            write_to_file(num1, num2, operator, result)
        elif choice == '2':
            filename = input("Enter the file name: ")
            print(read_from_file(filename))
        elif choice == '3':
            print("\nThanks for using the hyperion calcufiles, Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    calculator()


