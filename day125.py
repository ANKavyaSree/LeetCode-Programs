def lexicographically_smallest_array(nums, limit):
    n = len(nums)
    arr = sorted((value, i) for i, value in enumerate(nums))
    result = nums[:]
    i = 0

    while i < n:
        j = i

        while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
            j += 1

        values = [arr[k][0] for k in range(i, j + 1)]
        indices = sorted(arr[k][1] for k in range(i, j + 1))

        for k in range(len(indices)):
            result[indices[k]] = values[k]

        i = j + 1

    return result


# User input
nums = list(map(int, input("Enter nums separated by spaces: ").split()))
limit = int(input("Enter limit: "))

print(lexicographically_smallest_array(nums, limit))
