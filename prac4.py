# Q1
for iter in range(1, 11):
    print(iter)

for iter in range(2, 11, 2):
    print(iter)

# Q2
iter = 1

while iter <= 10:
    print(iter)
    iter += 1

# Q3
numbers = int(input("Enter number count: "))
sum = 0
iter = 1

while iter <= numbers:
    number = int(input("Enter a number: "))
    sum = sum + number
    iter += 1

print("Sum =", sum)
print("Average =", sum / numbers)

# Q4
number = int(input("Enter a number: "))
fact = 1
iter = 1

while iter <= number:
    fact = fact * iter
    iter += 1

print("Factorial =", fact)


# Q5
number = int(input("Enter a number: "))
iter = 1

while iter <= 10:
    print(number, "x", iter, "=", number * iter)
    iter += 1

# Q6
number = int(input("Enter a number: "))
org_number = number
rev_num = 0

while number > 0:
    mod = number % 10
    rev_num = rev_num * 10 + mod
    number = number // 10

print("Reverse number:", rev_num)

if org_number == rev_num:
    print(org_number, "is palindrome")
else:
    print(org_number, "is not palindrome")

    
# Q7
number = int(input("Enter a number: "))
tot_count = 0
even_count = 0
odd_count = 0

while number > 0:
    mod = number % 10
    tot_count += 1

    if mod % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    number = number // 10

print("Total number of digits:", tot_count)
print("Total even digits:", even_count)
print("Total odd digits:", odd_count)

# Q8
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

# Q9
n = int(input("Enter number of terms: "))
a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# Q10
# by star pattern
rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# by reverse star pattern
rows = 4

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# by number pattern
rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()