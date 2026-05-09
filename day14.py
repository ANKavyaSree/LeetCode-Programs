# Function to rotate each layer of the grid
def rotateGrid(grid, k):

    m = len(grid)
    n = len(grid[0])

    layers = min(m, n) // 2

    for layer in range(layers):

        elements = []

        # Top row
        for j in range(layer, n - layer):
            elements.append(grid[layer][j])

        # Right column
        for i in range(layer + 1, m - layer - 1):
            elements.append(grid[i][n - layer - 1])

        # Bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            elements.append(grid[m - layer - 1][j])

        # Left column
        for i in range(m - layer - 2, layer, -1):
            elements.append(grid[i][layer])

        # Rotate elements
        k_rotate = k % len(elements)
        rotated = elements[k_rotate:] + elements[:k_rotate]

        index = 0

        # Fill Top row
        for j in range(layer, n - layer):
            grid[layer][j] = rotated[index]
            index += 1

        # Fill Right column
        for i in range(layer + 1, m - layer - 1):
            grid[i][n - layer - 1] = rotated[index]
            index += 1

        # Fill Bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            grid[m - layer - 1][j] = rotated[index]
            index += 1

        # Fill Left column
        for i in range(m - layer - 2, layer, -1):
            grid[i][layer] = rotated[index]
            index += 1

    return grid


# User Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter matrix elements row by row:")

for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

k = int(input("Enter number of rotations: "))

result = rotateGrid(grid, k)

print("Rotated Grid:")

for row in result:
    print(*row)


# sample input
# Enter number of rows: 4
# Enter number of columns: 4
# Enter matrix elements row by row:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Enter number of rotations: 2

# sample output
# Rotated Grid:
# 3 4 8 12
# 2 11 10 16
# 1 7 6 15
# 5 9 13 14