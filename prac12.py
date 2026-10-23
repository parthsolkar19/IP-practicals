# Q1
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


# Q2
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result =", num1 / num2)
except ValueError:
    print("Error: Please enter valid integers")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# Q3
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Division Result =", result)
    print("Operation completed successfully")


# Q4
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")


# Q5
try:
    number = int(input("Enter a number: "))
    print(100 / number)
except Exception as e:
    print("Error:", e)


# Q6
while True:
    try:
        number = int(input("Enter an integer: "))
        print("You entered:", number)
        break
    except ValueError:
        print("Invalid input! Please enter an integer")


# Q7
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result =", num1 / num2)
except ValueError:
    print("Please enter only numeric values")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter another number")


# Q8
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise Exception("You are not eligible")
    print("You are eligible")
except Exception as e:
    print(e)


# Q9
class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100")
    print("Valid marks")
except InvalidMarksError as e:
    print(e)


# Q10
balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise Exception("Insufficient balance")
    balance -= amount
    print("Withdrawal successful")
    print("Remaining Balance:", balance)
except Exception as e:
    print(e)


# Q11 - Program 1: Multiple except blocks
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")


# Q11 - Program 2: Generic Exception
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except Exception as e:
    print("Error:", e)


# Q12
try:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print("Division Result =", result)

        numbers = [10, 20, 30]
        index = int(input("Enter list index: "))
        print("Element =", numbers[index])

    except ZeroDivisionError:
        print("Cannot divide by zero")
    except IndexError:
        print("Invalid index for list")
    except ValueError:
        print("Invalid input")

except Exception as e:
    print("Error:", e)