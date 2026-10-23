# Q1
student = {
    "Name": "Asha",
    "Age": 18,
    "Marks": 85
}

print(student)
print(type(student))


# Q2
student = {"Name": "Asha", "Age": 18, "Marks": 85}

print(student["Name"])
print(student["Marks"])
print(student["Grade"])


# Q3
student = {"Name": "Asha", "Age": 18, "Marks": 85}

print(student.get("Name"))
print(student.get("Grade", "Not found"))
print(student["Age"])


# Q4
student = {"Name": "Asha", "Age": 18, "Marks": 85}

student["Grade"] = "A"
student["Marks"] = 90

print(student)


# Q5
student = {"Name": "Asha", "Age": 18, "Marks": 85}

student.pop("Age")
del student["Marks"]

print(student)

student.pop("Grade")


# Q6
student = {"Name": "Asha", "Age": 18, "Marks": 85}

print("Keys:")
for key in student:
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-value pairs:")
for key, value in student.items():
    print(key, value)


# Q7
student = {"Name": "Asha", "Age": 18, "Marks": 85}

keys = list(student.keys())
values = list(student.values())
items = list(student.items())

print(keys)
print(values)
print(items)


# Q8
text = input("Enter string: ")
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


# Q9
students = {
    "S1": {"Name": "Asha", "Marks": 85},
    "S2": {"Name": "Ravi", "Marks": 90}
}

print(students["S1"]["Name"])

students["S1"]["Marks"] = 95

print(students)


# Q10
d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 3}

d1.update(d2)

print(d1)


# Q11
data = {"c": 3, "a": 1, "b": 2}

print(dict(sorted(data.items())))

print(dict(sorted(data.items(), key=lambda x: x[1])))


# Q12
inventory = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

inventory["Printer"] = 5
inventory["Laptop"] += 5

del inventory["Mouse"]

print(inventory)