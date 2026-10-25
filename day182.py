# day182.py
# Number of Closed Islands - User Input Program

def closedIsland(grid):
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        if grid[r][c] == 1:
            return True

        grid[r][c] = 1

        up = dfs(r - 1, c)
        down = dfs(r + 1, c)
        left = dfs(r, c - 1)
        right = dfs(r, c + 1)

        return up and down and left and right

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and dfs(r, c):
                count += 1

    return count


# Input format:
# First line: number of rows and columns (m n)
# Next m lines: n space-separated values (0 or 1)
m, n = map(int, input().split())
grid = []

for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

print(closedIsland(grid))
