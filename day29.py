def maxJumps(arr, d):
    n = len(arr)
    dp = [0] * n

    def dfs(i):
        if dp[i]:
            return dp[i]

        max_jump = 1

        # Move Right
        for j in range(i + 1, min(n, i + d + 1)):
            if arr[j] >= arr[i]:
                break
            max_jump = max(max_jump, 1 + dfs(j))

        # Move Left
        for j in range(i - 1, max(-1, i - d - 1), -1):
            if arr[j] >= arr[i]:
                break
            max_jump = max(max_jump, 1 + dfs(j))

        dp[i] = max_jump
        return dp[i]

    result = 0
    for i in range(n):
        result = max(result, dfs(i))

    return result


# User Input
arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter d value: "))

print("Maximum indices that can be visited:", maxJumps(arr, d))

# sample input
# Enter array elements: 6 4 14 6 8 13 9 7 10 6 12
# Enter d value: 2

# sample output
# Maximum indices that can be visited: 4