# Day 185 - Minimum XOR Value Among Valid Grid Paths
# User-input Python program

def minCost(grid):
    m, n = len(grid), len(grid[0])

    dp = [[set() for _ in range(n)] for _ in range(m)]
    dp[0][0].add(grid[0][0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if i > 0:
                for x in dp[i - 1][j]:
                    dp[i][j].add(x ^ grid[i][j])

            if j > 0:
                for x in dp[i][j - 1]:
                    dp[i][j].add(x ^ grid[i][j])

    return min(dp[m - 1][n - 1])


# Input format:
# First line: m n
# Next m lines: n integers in each row
# Example:
# 2 2
# 1 2
# 3 4

m, n = map(int, input().split())
grid = []

for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

print(minCost(grid))
