def maximum_total_value(nums, k):
    # Maximum value of any subarray = max(nums) - min(nums)
    max_diff = max(nums) - min(nums)

    # Since the same subarray can be chosen multiple times,
    # choose the subarray with maximum value k times.
    return max_diff * k


# User Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter value of k: "))

result = maximum_total_value(nums, k)

print("Maximum Total Value:", result)


# sample input
# Enter array elements: 1 3 2
# Enter value of k: 2

# sample output
# Maximum Total Value: 4