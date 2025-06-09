"""
Matrix multiplication

"""

a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8], [9, 10], [11, 12]]

# Get dimensions of the matrices
rows_a = len(a)
cols_a = len(a[0])
rows_b = len(b)
cols_b = len(b[0])

# Check if multiplication is possible
if cols_a != rows_b:
    print("Number of columns in A must equal number of rows in B")
    exit(1)

# Initialize result matrix with zeros
result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

# Perform multiplication
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result[i][j] += a[i][k] * b[k][j]


print(result)