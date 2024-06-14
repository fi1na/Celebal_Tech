def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return num1 / num2


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation_choice = input("Enter choice (1/2/3/4): ")

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if operation_choice == '1':
    print(first_number, "+", second_number,
          "=", add(first_number, second_number))
elif operation_choice == '2':
    print(first_number, "-", second_number, "=",
          subtract(first_number, second_number))
elif operation_choice == '3':
    print(first_number, "*", second_number, "=",
          multiply(first_number, second_number))
elif operation_choice == '4':
    print(first_number, "/", second_number, "=",
          divide(first_number, second_number))
else:
    print("Invalid input")
