# Day 200 - Longest Strictly Increasing or Strictly Decreasing Subarray

def longestMonotonicSubarray(nums):
    inc = 1
    dec = 1
    ans = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc += 1
            dec = 1
        elif nums[i] < nums[i - 1]:
            dec += 1
            inc = 1
        else:
            inc = 1
            dec = 1

        ans = max(ans, inc, dec)

    return ans


# User input
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

result = longestMonotonicSubarray(nums)
print("Length of longest strictly increasing or decreasing subarray:", result)
