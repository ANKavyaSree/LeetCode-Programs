def maximumJumps(nums, target):
    n = len(nums)

    # dp[i] stores maximum jumps to reach index i
    dp = [-1] * n
    dp[0] = 0

    for i in range(n):
        if dp[i] == -1:
            continue

        for j in range(i + 1, n):
            if abs(nums[j] - nums[i]) <= target:
                dp[j] = max(dp[j], dp[i] + 1)

    return dp[-1]


# User Input
nums = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter target value: "))

# Function Call
result = maximumJumps(nums, target)

# Output
print("Maximum number of jumps:", result)

# sample input
# Enter array elements separated by space: 1 3 6 4 1 2
# Enter target value: 2

# sample output
# Maximum number of jumps: 3