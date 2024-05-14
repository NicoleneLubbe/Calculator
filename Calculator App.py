# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

# Main function 
def calculator():
    print("Simple Calculator")
    print("Enter 'quit' to exit")
    
    while True:
        # Take input from the user
        operation = input("Enter operation (+, -, *, /): ")
        
        # Check if user wants to quit
        if operation.lower() == 'quit':
            print("Exiting the calculator...")
            break
        
        # Check if operation is valid
        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation!")
            continue
        
        # Take input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform operation and print result
        if operation == '+':
            print("Result:", add(num1, num2))
        elif operation == '-':
            print("Result:", subtract(num1, num2))
        elif operation == '*':
            print("Result:", multiply(num1, num2))
        elif operation == '/':
            print("Result:", divide(num1, num2))

# Call the calculator function
calculator()



