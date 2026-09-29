# day156.py
# Valid Parentheses Path in a Grid

m, n = map(int, input("Enter m and n: ").split())

grid = []
print("Enter the grid rows:")
for _ in range(m):
    grid.append(input().split())

if (m + n - 1) % 2 != 0:
    print(False)
    exit()

dp = [[set() for _ in range(n)] for _ in range(m)]

if grid[0][0] == ')':
    print(False)
    exit()

dp[0][0].add(1)

for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            continue

        balances = set()

        if i > 0:
            balances.update(dp[i - 1][j])

        if j > 0:
            balances.update(dp[i][j - 1])

        for balance in balances:
            new_balance = balance + (1 if grid[i][j] == '(' else -1)

            if new_balance >= 0:
                dp[i][j].add(new_balance)

print(0 in dp[m - 1][n - 1])
