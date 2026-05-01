def maxRotateFunction(nums):
    n = len(nums)
    total_sum = sum(nums)

    # F(0)
    f = sum(i * nums[i] for i in range(n))
    res = f

    # Use relation:
    # F(k) = F(k-1) + total_sum - n * nums[n-k]
    for k in range(1, n):
        f = f + total_sum - n * nums[n - k]
        res = max(res, f)

    return res


# -------- User Input --------
n = int(input("Enter size of array: "))
print("Enter array elements:")
nums = list(map(int, input().split()))

print("Maximum Rotate Function Value:", maxRotateFunction(nums))


# Sample input
# Enter size of array: 4
# Enter array elements:
# 4 3 2 6


# sample output
# Maximum Rotate Function Value: 26