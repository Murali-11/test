# Simple Calculator Program
# Created for testing GitHub functionality

def calculator():
    print("Welcome to the Simple Calculator!")
    print("================================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    try:
        # Get user input
        choice = int(input("Enter choice (1-4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform calculation based on choice
        if choice == 1:
            result = num1 + num2
            operation = "+"
        elif choice == 2:
            result = num1 - num2
            operation = "-"
        elif choice == 3:
            result = num1 * num2
            operation = "*"
        elif choice == 4:
            if num2 == 0:
                return "Error: Cannot divide by zero"
            result = num1 / num2
            operation = "/"
        else:
            return "Invalid choice"
        
        # Return formatted result
        return f"{num1} {operation} {num2} = {result}"
        
    except ValueError:
        return "Invalid input: Please enter numbers only"

if __name__ == "__main__":
    print(calculator())
    print("\nThank you for using the calculator!")