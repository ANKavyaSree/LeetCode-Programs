# Day 198 - Minimum Cost to Reach the Top of the Staircase

n = int(input())
costs = list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(max(0, i - 3), i):
        dp[i] = min(
            dp[i],
            dp[j] + costs[i - 1] + (i - j) ** 2
        )

print(dp[n])
