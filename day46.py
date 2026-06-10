def maximum_total_subarray_value(nums, k):
    values = []

    n = len(nums)

    for i in range(n):
        curr_min = nums[i]
        curr_max = nums[i]

        for j in range(i, n):
            curr_min = min(curr_min, nums[j])
            curr_max = max(curr_max, nums[j])

            values.append(curr_max - curr_min)

    values.sort(reverse=True)

    return sum(values[:k])


# User Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

result = maximum_total_subarray_value(nums, k)

print("Maximum Total Subarray Value:", result)


# sample input
# Enter array elements: 1 3 2
# Enter k: 2

# sample output
# Maximum Total Subarray Value: 4