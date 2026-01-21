# Write a function to convert temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
fahrenheit = celsius_to_fahrenheit(100)
print("Temperature in Fahrenheit:", fahrenheit)




# Write a function to print all prime numbers between given range
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



# Write a function to print fibonacci series
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series



# Write a function to check the given string is palindrome or not
def is_palindrome(s):
    return s == s[::-1]



# Method-Based Calculator Engine
class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
        


 # Then use a loop-driven menu to run the calculator
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    user_input = input(": ")
    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if user_input == "add":
            print("Result:", Calculator().add(num1, num2))
        elif user_input == "subtract":
            print("Result:", Calculator().subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", Calculator().multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", Calculator().divide(num1, num2))
    else:
        print("Invalid input. Please try again.")


