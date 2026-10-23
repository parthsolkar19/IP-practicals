# Q1
nm = input("Enter your name: ")
ag = input("Enter your age: ")

print("Name:", nm)
print("Age:", ag)

# Formatted string (f-string)
print(f"Name: {nm}, Age: {ag}")


# Q2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Difference:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division by zero is not allowed")


# Q3
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("Sum:", a + b + c)
print("Average:", (a + b + c) / 3)
print("Expression:", (a + b) * c / 2)


# Q4
print(10 + 5 * 2)
print((10 + 5) * 2)
print(100 / 5 + 3 * 2)


# Q5
basic_sal = float(input("Enter basic salary: "))

hra = 0.2 * basic_sal
da = 0.1 * basic_sal
net_salary = basic_sal + hra + da

print("Basic salary:", basic_sal)
print("HRA:", hra)
print("DA:", da)
print("Net salary:", net_salary)



# Q6
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

pi = 3.14

area = length * breadth
perimeter = 2 * (length + breadth)
circumference = 2 * pi * radius

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)
print("Circumference of circle:", circumference)


# Q7
distance_km = float(input("Enter distance in km: "))
celsius = float(input("Enter temperature in Celsius: "))
rupees = float(input("Enter rupees: "))

fahrenheit = (celsius * 9 / 5) + 32
meters = distance_km * 1000
dollars = rupees / 95.5

print("Distance in meters:", meters)
print("Temperature in Fahrenheit:", fahrenheit)
print("Dollars:", dollars)


# Q8
a, b = map(float, input("Enter two numbers separated by space: ").split())

print("Sum:", a + b)
print("Product:", a * b)

if b != 0:
    div = a / b
    print("Result of division:", div)
else:
    print("Cannot divide by zero")

# Q9
subject1 = float(input("Enter marks for sub1: "))
subject2 = float(input("Enter marks for sub2: "))
subject3 = float(input("Enter marks for sub3: "))

total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

print("Total marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 75:
    print("Grade: A")
elif percentage >= 65:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Result: Fail")


# Q9
subject1 = float(input("Enter marks for sub1: "))
subject2 = float(input("Enter marks for sub2: "))
subject3 = float(input("Enter marks for sub3: "))

total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

print("Total marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 75:
    print("Grade: A")
elif percentage >= 65:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Result: Fail")


# Q10
# String concatenation
message = "Midrini" + "Patil"
print(message)

# String + number error
try:
    result = "Midrini" + 10
    print(result)
except TypeError:
    print("Error: Cannot add string and number")

# Division by zero error
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")