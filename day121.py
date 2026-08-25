def missing_multiple(nums, k):
    nums_set = set(nums)

    multiple = k

    while multiple in nums_set:
        multiple += k

    return multiple


# User input
nums = list(map(int, input("Enter nums separated by spaces: ").split()))
k = int(input("Enter k: "))

print(missing_multiple(nums, k))
