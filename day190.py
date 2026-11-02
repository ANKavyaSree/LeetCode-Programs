# Day 190 - LeetCode 462: Minimum Moves to Equal Array Elements II

def min_moves_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2]

    moves = 0
    for num in nums:
        moves += abs(num - median)

    return moves


# User input
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

print("Minimum moves:", min_moves_to_equal(nums))
