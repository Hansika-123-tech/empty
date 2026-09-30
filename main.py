import sys
from calculator import add, subtract, multiply, divide

def print_menu():
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("------------------")

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    while True:
        print_menu()
        choice = input("Select an operation (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            sys.exit(0)

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please select a valid option from the menu.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == '1':
                result = add(num1, num2)
                op = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op = '/'

            print(f"\nResult: {num1} {op} {num2} = {result}")

        except ValueError as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
