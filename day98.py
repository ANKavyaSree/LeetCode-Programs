n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the elements: ").split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = nums[i]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

print("Player 1 can win:", dp[0][n - 1] >= 0)
