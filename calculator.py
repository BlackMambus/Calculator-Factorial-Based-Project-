def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def calculator():
    print("🧮 Simple Python Calculator")
    print("Operations: +, -, *, /, ** (power), % (modulus)")

    while True:
        op = input("\nEnter operation (+, -, *, /, **, %, or 'q' to quit): ")
        if op == 'q':
            print("Goodbye!")
            break

        if op not in ['+', '-', '*', '/', '**', '%']:
            print("Invalid operation. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        elif op == '**':
            result = power(num1, num2)
        elif op == '%':
            result = modulus(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()

