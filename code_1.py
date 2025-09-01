class Calculator:
    """
    A simple calculator class supporting basic arithmetic operations.
    """

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        if b == 0:
            return "Error: Division by zero in modulus"
        return a % b

def get_number(prompt):
    """
    Prompt the user for a number and handle invalid input.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    calc = Calculator()
    operations = {
        "1": ("Addition", calc.add),
        "2": ("Subtraction", calc.subtract),
        "3": ("Multiplication", calc.multiply),
        "4": ("Division", calc.divide),
        "5": ("Power", calc.power),
        "6": ("Modulus", calc.modulus)
    }

    print("\n--- Python Calculator ---")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("7. Exit")

    while True:
        choice = input("\nEnter choice (1-7): ")
        if choice == "7":
            print("Exiting... Goodbye 👋")
            break
        if choice not in operations:
            print("Invalid choice! Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"{operation_name} result: {result}")

if __name__ == "__main__":
    main()