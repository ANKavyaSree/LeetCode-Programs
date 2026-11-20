# Day 207 - LeetCode 1509
# Minimum Difference Between Largest and Smallest Value in Three Moves

def minimizeSum(nums):
    nums.sort()

    return min(
        nums[-1] - nums[2],
        nums[-2] - nums[1],
        nums[-3] - nums[0]
    )


# User input
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

result = minimizeSum(nums)
print("Minimum possible difference:", result)
