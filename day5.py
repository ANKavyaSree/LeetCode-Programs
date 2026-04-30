def maxPathScore(grid, k):
    m, n = len(grid), len(grid[0])

    # dp[i][j][c] = max score reaching (i,j) with cost c
    dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]

    # Starting cell
    start_cost = 0 if grid[0][0] == 0 else 1
    if start_cost <= k:
        dp[0][0][start_cost] = grid[0][0]

    for i in range(m):
        for j in range(n):
            for cost in range(k+1):
                if dp[i][j][cost] == -1:
                    continue

                for di, dj in [(0,1), (1,0)]:  # right, down
                    ni, nj = i + di, j + dj

                    if ni < m and nj < n:
                        new_cost = cost + (0 if grid[ni][nj] == 0 else 1)

                        if new_cost <= k:
                            dp[ni][nj][new_cost] = max(
                                dp[ni][nj][new_cost],
                                dp[i][j][cost] + grid[ni][nj]
                            )

    result = max(dp[m-1][n-1])
    return result if result != -1 else -1


# -------- User Input --------
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
k = int(input("Enter max cost k: "))

print("Enter grid rows (values 0,1,2):")
grid = []

for _ in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

print("Maximum Score:", maxPathScore(grid, k))



##Sample input
# Enter number of rows: 2
# Enter number of columns: 2
# Enter max cost k: 1
# 0 1
# 2 0


##Sample output
# Maximum Score: 2