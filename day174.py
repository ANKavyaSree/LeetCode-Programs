# day174.py
# User-input program for LeetCode 3551:
# Minimum Swaps to Sort by Digit Sum

def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def min_swaps(nums):
    sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

    position = {num: i for i, num in enumerate(nums)}
    visited = [False] * len(nums)
    swaps = 0

    for i in range(len(nums)):
        if visited[i] or sorted_nums[i] == nums[i]:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = position[sorted_nums[j]]
            cycle_size += 1

        swaps += cycle_size - 1

    return swaps


if __name__ == "__main__":
    # Enter distinct positive integers separated by spaces.
    # Example: 18 43 34 16
    nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
    print("Minimum swaps:", min_swaps(nums))
