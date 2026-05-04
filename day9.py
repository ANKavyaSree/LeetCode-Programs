# Rotate Image (90 degrees clockwise, in-place)

def rotate(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix


# -------- User Input --------
n = int(input("Enter size of matrix (n x n): "))

print("Enter matrix rows:")
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

rotated = rotate(matrix)

print("Rotated Matrix:")
for row in rotated:
    print(*row)

# sample input
# Enter size of matrix (n x n): 3
# Enter matrix rows:
# 1 2 3
# 4 5 6
# 7 8 9

# sample output
# Rotated Matrix:
# 7 4 1
# 8 5 2
# 9 6 3