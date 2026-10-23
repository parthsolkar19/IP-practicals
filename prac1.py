# Q1
name="Midrini"
age=18
marks=99.5
city="Pune"
print(name,age,marks,city)


# Q2
value=100
print(value)
print(type(value))
value="Midrini"
print(value)
print(type(value))
value=5.5
print(value)
print(type(value))


# Q3
PI=3.14159
GRAVITY=9.8
MAX_USERS=100
print("PI:",PI)
print("GRAVITY:",GRAVITY)
print("MAX_USERS:",MAX_USERS)


# Q4
integer = int(input("Enter an integer: "))
floating = float(input("Enter a float: "))
string = input("Enter a string: ")
boolean = input("Enter True or False: ")
boolean = boolean == "True"
print("\nSummary")
print("------------")
print(integer, "\t", type(integer))
print(floating, "\t", type(floating))
print(string, "\t", type(string))
print(boolean, "\t", type(boolean))


# Q5
age = input("Enter your age: ")
marks = int(input("Enter your marks: "))
print("Without conversion")
print(age + "marks")
age = int(age)
print("Age after conversion:", age + 5)
print("Marks+2:", marks + 2)


# Q6
a = 10
b = 5.5
print(a + b)  # Implicit conversion
# print(a + "5")  # Type Error
c = "5"
print(a + int(c))  # Explicit conversion


# Q7
a=100
b=100
print(id(a))
print(id(b))
b=200
print(id(b))


# Q8
a=10
b=20
temp=a
a=b
b=temp
print(a,b)
a=10
b=20
a,b=b,a
print(a,b)


# Q9
first = input("Enter first value: ")
second = input("Enter second value: ")

try:
    num1 = float(first)
    num2 = float(second)
    print("Addition:", num1 + num2)

except ValueError:
    if first.isalpha() and second.isalpha():
        print("Concatenation:", first + second)
    else:
        print("Invalid Input")


# Q10
age = int(input("Enter Age: "))
marks = int(input("Enter marks: "))

isAdult = age > 18
isPassed = marks > 50

print("Is Adult:", isAdult)
print("Is Passed:", isPassed)

if isAdult and isPassed:
    print("Eligible")
else:
    print("Not Eligible")


# Q11
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")