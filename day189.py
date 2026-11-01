def min_moves(nums):
    minimum = min(nums)
    return sum(num - minimum for num in nums)


if __name__ == "__main__":
    # Enter the number of elements
    n = int(input())

    # Enter the array elements separated by spaces
    nums = list(map(int, input().split()))

    if len(nums) != n:
        raise ValueError("Please enter exactly n array elements.")

    print(min_moves(nums))
