# day172.py
# Subarrays Distinct Element Sum of Squares I

def sum_counts(nums):
    total = 0
    n = len(nums)

    for i in range(n):
        distinct = set()
        for j in range(i, n):
            distinct.add(nums[j])
            total += len(distinct) ** 2

    return total


if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
    print("Sum of squares of distinct counts:", sum_counts(nums))
