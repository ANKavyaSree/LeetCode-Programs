def minimum_deletions(nums):
    n = len(nums)

    min_index = nums.index(min(nums))
    max_index = nums.index(max(nums))

    left = min(min_index, max_index)
    right = max(min_index, max_index)

    front = right + 1
    back = n - left
    both = (left + 1) + (n - right)

    return min(front, back, both)


# User input
nums = list(map(int, input("Enter nums separated by spaces: ").split()))

print(minimum_deletions(nums))
