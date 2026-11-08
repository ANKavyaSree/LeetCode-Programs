def countServers(grid):
    m = len(grid)
    n = len(grid[0])

    rows = [0] * m
    cols = [0] * n

    # Count servers in each row and column.
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                rows[i] += 1
                cols[j] += 1

    # Count servers that communicate with another server.
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                ans += 1

    return ans


if __name__ == "__main__":
    m, n = map(int, input("Enter number of rows and columns: ").split())

    grid = []
    print("Enter the grid rows (0s and 1s separated by spaces):")
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)

    print("Number of communicating servers:", countServers(grid))
