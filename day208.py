# Day 208 - LeetCode 3041
# Maximize Consecutive Elements in an Array After Modification

def maxSelectedElements(nums):
    nums.sort()

    dp = {}
    ans = 0

    for num in nums:
        dp[num + 1] = dp.get(num, 0) + 1
        dp[num] = dp.get(num - 1, 0) + 1

        ans = max(ans, dp[num], dp[num + 1])

    return ans


# User input
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

result = maxSelectedElements(nums)
print("Maximum number of consecutive elements:", result)
