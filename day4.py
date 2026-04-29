# Maximum Score From Grid Operations
# Dynamic Programming Approach

def maximumScore(grid):
    n = len(grid)

    # Prefix sums for quick column calculations
    prefix = [[0]*n for _ in range(n+1)]
    for c in range(n):
        for r in range(n):
            prefix[r+1][c] = prefix[r][c] + grid[r][c]

    # dp[col][height] = max score after processing columns
    dp = [[0]* (n+1) for _ in range(n)]

    for h in range(n+1):
        dp[0][h] = 0

    for col in range(1,n):
        for curr in range(n+1):
            best = 0
            for prev in range(n+1):
                gain = 0

                if curr > prev:
                    gain = prefix[curr][col-1] - prefix[prev][col-1]
                elif prev > curr:
                    gain = prefix[prev][col] - prefix[curr][col]

                best = max(best, dp[col-1][prev] + gain)

            dp[col][curr] = best

    return max(dp[n-1])


# -------- User Input --------
n = int(input("Enter size of square grid (n): "))

print("Enter grid rows:")
grid=[]
for _ in range(n):
    row=list(map(int,input().split()))
    grid.append(row)

print("Maximum Score:", maximumScore(grid))


#Sample input
# Enter size of square grid (n): 5
# 10 0 0 0 0
# 0 0 3 0 0
# 0 1 0 0 0
# 5 0 0 3 0
# 0 0 0 0 2


#sample output
#Maximum Score: 11