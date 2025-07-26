try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Unknown operation!")
    print("Result:", result)

except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a number!")
except Exception as e:
    print("Something went wrong:", e)
finally:
    print("Program finished.")
