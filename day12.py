def maxReachable(nums):
    n = len(nums)
    ans = [0] * n

    # Traverse from right to left
    max_so_far = nums[-1]

    for i in range(n - 1, -1, -1):
        max_so_far = max(max_so_far, nums[i])
        ans[i] = max_so_far

    return ans


# -------- User Input --------
nums = list(map(int, input("Enter array elements: ").split()))

result = maxReachable(nums)

print("Maximum reachable values:")
print(*result)


# sample input
# Enter array elements: 2 1 3

# sample output
# Maximum reachable values:
# 2 2 3