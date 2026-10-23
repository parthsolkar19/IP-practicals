# Q1
file = open("sample.txt", "w")
file.write("Hello world!\n")
file.write("Welcome to Python\n")
file.write("File Handling Example")
file.close()


# Q2
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()


# Q3
file = open("sample.txt", "r")

print(file.readline())
print(file.readline())

file.close()

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()


# Q4
# Writing
with open("sample.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("File Handling Example\n")

# Reading
with open("sample.txt", "r") as file:
    print(file.read())


# Q5
with open("sample.txt", "a") as file:
    file.write("This line is appended.\n")
    file.write("This old content remains.\n")

with open("sample.txt", "r") as file:
    print(file.read())


# Q6
with open("sample.txt", "r") as file:
    content = file.read()

lines = content.split("\n")
words = content.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(content))


# Q7
word = input("Enter word to search: ")

with open("sample.txt", "r") as file:
    content = file.read()

count = content.lower().count(word.lower())
print("Occurrences:", count)


# Q8
with open("sample.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("File copied successfully")

with open("copy.txt", "r") as file:
    print(file.read())


# Q9
keyword = input("Enter keyword: ")

with open("sample.txt", "r") as source, \
     open("filtered.txt", "w") as destination:

    for line in source:
        if keyword.lower() in line.lower():
            destination.write(line)

print("Filtered file created!")


# Q10
with open("students.txt", "w") as file:
    file.write("101 Rahul 85\n")
    file.write("102 Priya 92\n")
    file.write("103 Amit 78\n")

print("Student Records")

with open("students.txt", "r") as file:
    for line in file:
        roll, name, marks = line.split()
        print(f"Roll No: {roll}, Name: {name}, Marks: {marks}")


# Q11
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File does not exist")

except Exception as e:
    print("Error:", e)


# Q12
with open("sample.txt", "r") as file:
    content = file.read()

content = content.replace("Python", "Java")

with open("sample.txt", "w") as file:
    file.write(content)

print("File updated successfully")

with open("sample.txt", "r") as file:
    print(file.read())