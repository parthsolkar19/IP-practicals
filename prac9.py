# Q1
def display_message():
    print("Welcome to Python Functions")

display_message()
display_message()
display_message()


# Q2
def add(a, b):
    print("Sum:", a + b)

add(10, 20)
add(5, 7)


# Q3
def square(num):
    return num * num

result = square(5)

print("Square:", result)
print("Square plus 10:", result + 10)


# Q4
def student(name, age=18):
    print("Name:", name)
    print("Age:", age)

# Positional argument
student("Rahul")

# Keyword argument
student(age=20, name="Priya")


# Q5
numbers = [10, 20, 30, 40, 50]
text = "Python"

print("Length of list:", len(numbers))
print("Length of string:", len(text))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

total = 0
for n in numbers:
    total += n

print("Manual sum:", total)


# Q6
def process_list(lst):
    print("Sum:", sum(lst))
    print("Largest:", max(lst))

list1 = [10, 20, 30]
list2 = [5, 15, 25, 35]

process_list(list1)
process_list(list2)


# Q7
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
print("Factorial:", factorial(num))

# Loop-Based Approach
fact = 1

for i in range(1, 6):
    fact *= i

print("Factorial:", fact)


# Q8
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = 7

for i in range(terms):
    print(fibonacci(i), end=" ")


# Q9
def get_number():
    return int(input("Enter a number: "))

def square(num):
    return num * num

def display_result(result):
    print("Square:", result)

def main():
    n = get_number()
    result = square(n)
    display_result(result)

main()


# Q10
count = 10

def show():
    global count
    count += 5
    print("Inside function:", count)

show()
print("Outside function:", count)


# Q11
def addition():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)

def prime():
    n = int(input("Enter a number: "))

    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return

    print("Prime")

def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print("Factorial:", fact)

print("1. Addition")
print("2. Prime Check")
print("3. Factorial")

choice = int(input("Enter choice: "))

if choice == 1:
    addition()
elif choice == 2:
    prime()
elif choice == 3:
    factorial()
else:
    print("Choice Invalid")


# Q12
def input_marks():
    marks = []

    for i in range(5):
        marks.append(int(input(f"Enter marks for subject {i + 1}: ")))

    return marks

def calculate(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage

def grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

def main():
    marks = input_marks()
    total, percentage = calculate(marks)

    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade(percentage))

main()