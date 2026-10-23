# Q1
for num in range(1, 11):
    if num == 5:
        break
    print(num)


# Q2
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)


# Q3
for num in range(1, 11):
    if num == 5:
        break
    print(num)

for num in range(1, 11):
    if num == 5:
        continue
    print(num)

# Q4
numbers = [10, 20, 30, 40, 50, 60]
target = 40

for i, num in enumerate(numbers):
    if num == target:
        print(f"Item found at position {i}")
        break


# Q5
n = int(input("Enter a number: "))

for i in range(1, 101):
    if i % n == 0:
        print(f"First number divisible by {n} is {i}")
        break

# Q6
numbers = [10, -5, 20, -1, 30, 40]

for num in numbers:
    if num < 0:
        continue
    print(num)

    
# Q7
total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    if num < 0:
        continue

    total += num

print(f"Sum of valid inputs: {total}")

# Q8
correct_pass = "Python123"
attempts = 3

for attempt in range(1, attempts + 1):
    pwd = input("Enter password: ")

    if pwd == correct_pass:
        print("Access granted")
        break

    print(f"Wrong! Attempts left: {attempts - attempt}")

else:
    print("Access denied, 3 wrong attempts")

# Q9
for i in range(5):
    if i == 3:
        pass
    print(i)


# Q10
for i in range(1,6):
    if i %2==0
    continue
print(i,end=" ")
print()