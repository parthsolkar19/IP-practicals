# Q1
numbers = [10, 20, 30, 40]
names = ("Alice", "Bob", "Charlie")

print(numbers)
print(names)
print(type(numbers))
print(type(names))


# Q2
list1 = [10, 20, 30, 40, 50]
tup = ("A", "B", "C", "D", "E")

print(list1[0], list1[-1], list1[2])
print(tup[0], tup[-1], tup[2])

print(list1[-5], list1[-1])
print(tup[-5], tup[-1])


# Q3
list1 = [10, 20, 30, 40, 50]
tup = (10, 20, 30, 40, 50)

print(list1[:3])
print(list1[-2:])
print(list1[::2])

print(tup[:3])
print(tup[-2:])
print(tup[::2])


# Q4
list1 = [10, 20, 30]
tup = (10, 20, 30)

list1[0] = 100
print(list1)

try:
    tup[0] = 100
except TypeError:
    print("Tuple cannot be modified")


# Q5
list1 = [10, 20, 30]

list1.append(40)
list1.insert(1, 15)

print(list1)


# Q6
list1 = [10, 20, 30, 40]

list1.remove(20)
list1.pop()

print(list1)

try:
    list1.remove(50)
except ValueError:
    print("Element not present")


# Q7
list1 = [40, 10, 30, 20]

list1.sort()
print("Ascending:", list1)

list1.sort(reverse=True)
print("Descending:", list1)

list1.reverse()
print("Reversed:", list1)


# Q8
tup = (10, 20, 30, 20, 10)

print("Count:", tup.count(20))
print("Index:", tup.index(30))

try:
    print(tup.index(50))
except ValueError:
    print("Element is not present")


# Q9
matrix = [[1, 2], [3, 4], [5, 6]]

print(matrix[1][0])

matrix[1][0] = 10

print(matrix)


# Q10
list1 = [10, 20, 30]

tup = tuple(list1)
print(tup)

list2 = list(tup)
list2[0] = 100

print(list2)


# Q11
list1 = [10, 20, 30, 40]
tup = (10, 20, 30, 40)

for x in list1:
    print(x)

print("Sum:", sum(list1))

for x in tup:
    print(x)


# Q12
cart = ["Apple", "Milk", "Bread"]
categories = ("Food", "Beverages", "Dairy")

cart.append("Juice")
cart.remove("Milk")

print("Cart:", cart)
print("Categories:", categories)
print("Total items:", len(cart))