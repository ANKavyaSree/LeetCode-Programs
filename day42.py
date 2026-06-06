def left_right_difference(nums):
    n = len(nums)

    left_sum = [0] * n
    right_sum = [0] * n
    answer = [0] * n

    # Calculate left sums
    for i in range(1, n):
        left_sum[i] = left_sum[i - 1] + nums[i - 1]

    # Calculate right sums
    for i in range(n - 2, -1, -1):
        right_sum[i] = right_sum[i + 1] + nums[i + 1]

    # Calculate absolute differences
    for i in range(n):
        answer[i] = abs(left_sum[i] - right_sum[i])

    return answer


# User Input
n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter elements separated by space: ").split()))

result = left_right_difference(nums)

print("Output:", result)

# sample input
# Enter number of elements: 4
# Enter elements separated by space: 10 4 8 3

# sample output
# Output: [15, 1, 11, 22]