def minimumSumSubarray(nums, l, r):
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    ans = float('inf')

    for i in range(n):
        for length in range(l, r + 1):
            j = i + length
            if j > n:
                break

            subarray_sum = prefix[j] - prefix[i]
            if subarray_sum > 0:
                ans = min(ans, subarray_sum)

    return ans if ans != float('inf') else -1


# User input
nums = list(map(int, input().split()))
l, r = map(int, input().split())

print(minimumSumSubarray(nums, l, r))
