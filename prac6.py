# Q1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Entire Matrix:")
for row in matrix:
    print(row)

print("First row:", matrix[0])
print("Element at (2,3):", matrix[1][2])


# Q2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Row-wise Traversal:")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()

print("\nColumn-wise Traversal:")
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()


# Q3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Row Sums:")
for i in range(len(matrix)):
    row_sum = sum(matrix[i])
    print(f"Row {i + 1} sum: {row_sum}")

print("\nColumn Sums:")
for j in range(len(matrix[0])):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][j]
    print(f"Column {j + 1}: {col_sum}")


# Q4
a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [10, 11, 12]]

c = []

for i in range(2):
    row = []
    for j in range(3):
        row.append(a[i][j] + b[i][j])
    c.append(row)

print(c)


# Q5
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

transpose = []

for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)


# Q6
import numpy as np

a = np.array([1, 2, 3])
b = np.zeros(3)
c = np.ones(3)

print(a, a.shape, a.dtype)
print(b, b.shape, b.dtype)
print(c, c.shape, c.dtype)


# Q7
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a[0, 2])
print(a[1])
print(a[:, 1])
print(a[0:2, 1:3])


# Q8
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)

x = [1, 2, 3]
y = [4, 5, 6]

print([x[i] + y[i] for i in range(3)])


# Q9
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Std:", np.std(a))


# Q10
import numpy as np

a = np.arange(1, 13)

print(a.reshape(3, 4))
print(a.reshape(4, 3))


# Q11
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Multiplication:\n", a @ b)
print("Transpose:\n", a.T)


# Q12
import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])

avg = np.mean(marks, axis=1)

print("Average:", avg)
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))