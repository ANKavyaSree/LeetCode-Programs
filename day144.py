def min_sum_of_lengths(arr, target):
    n = len(arr)

    best = [float('inf')] * n

    left = 0
    curr_sum = 0
    min_len = float('inf')
    answer = float('inf')

    for right in range(n):
        curr_sum += arr[right]

        while curr_sum > target:
            curr_sum -= arr[left]
            left += 1

        if curr_sum == target:
            length = right - left + 1

            if left > 0 and best[left - 1] != float('inf'):
                answer = min(answer, length + best[left - 1])

            min_len = min(min_len, length)

        if right == 0:
            best[right] = min_len
        else:
            best[right] = min(best[right - 1], min_len)

    return -1 if answer == float('inf') else answer


arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

result = min_sum_of_lengths(arr, target)

print("Minimum sum of lengths:", result)
