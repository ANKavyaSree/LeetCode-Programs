# day184.py
# Construct a grid with exactly one valid path
# User-input Python program

def create_grid(m, n):
    grid = [['#'] * n for _ in range(m)]

    # Keep the top row free.
    for j in range(n):
        grid[0][j] = '.'

    # Keep the rightmost column free.
    for i in range(m):
        grid[i][n - 1] = '.'

    return [''.join(row) for row in grid]


m, n = map(int, input("Enter m and n: ").split())

result = create_grid(m, n)

print("Grid:")
for row in result:
    print(row)

print("Output:", result)
