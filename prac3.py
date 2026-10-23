# Q1
num = int(input("Enter a number: "))

if num > 0:
    print(num, "is positive")

# Q2
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Q3
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Congratulations! You scored A grade")
elif marks >= 75:
    print("Good! You got B grade")
elif marks >= 50:
    print("Need improvement! You got C grade")
else:
    print("Oops! You failed")


# Q4
age = int(input("Enter age: "))
nationality = input("Enter nationality: ")

if age >= 18:
    if nationality == "Indian":
        print("You are eligible to vote")
    else:
        print("Not eligible due to nationality")
else:
    print("Not eligible due to age")



# Q5
num1, num2, num3 = map(
    int, input("Enter three numbers separated by space: ").split()
)

if num1 == num2 == num3:
    print("All numbers are equal")
elif num1 >= num2 and num1 >= num3:
    print(num1, "is greatest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")


# Q6
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


    
# Q7
num1, num2 = map(
    float, input("Enter two numbers separated by space: ").split()
)

op = input("Enter an operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# Q8
pur_amt = float(input("Enter purchase amount: "))

if pur_amt >= 2000:
    discount = pur_amt * 0.20
    print("Congratulations! You saved 20%")
elif pur_amt >= 1000:
    discount = pur_amt * 0.10
    print("Congratulations! You saved 10%")
else:
    discount = 0
    print("Sorry, no discount")

final_amount = pur_amt - discount

print("Discount:", discount)
print("Final amount:", final_amount)


# Q9
num1, num2, num3 = map(
    int, input("Enter three sides separated by space: ").split()
)

if num1 <= 0 or num2 <= 0 or num3 <= 0:
    print("Invalid sides")
elif num1 + num2 <= num3 or num1 + num3 <= num2 or num2 + num3 <= num1:
    print("Invalid triangle")
elif num1 == num2 == num3:
    print("The given triangle is Equilateral")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("The given triangle is Isosceles")
else:
    print("The given triangle is Scalene")


# Q10
print("----- MENU -----")
print("1. Check Even/Odd")
print("2. Find Largest")
print("3. Grade System")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a >= b and a >= c:
        print("Largest number is", a)
    elif b >= a and b >= c:
        print("Largest number is", b)
    else:
        print("Largest number is", c)

elif choice == 3:
    marks = int(input("Enter your marks: "))

    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    elif marks >= 35:
        print("Grade: D")
    else:
        print("Grade: Fail")

else:
    print("Invalid choice!")