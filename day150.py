# day150.py

def min_operations(nums, x):
    total = sum(nums)
    target = total - x
    n = len(nums)

    if target < 0:
        return -1

    if target == 0:
        return n

    left = 0
    current = 0
    max_len = -1

    for right in range(n):
        current += nums[right]

        while current > target and left <= right:
            current -= nums[left]
            left += 1

        if current == target:
            max_len = max(max_len, right - left + 1)

    return -1 if max_len == -1 else n - max_len


def main():
    nums = list(map(int, input("Enter nums: ").split()))
    x = int(input("Enter x: "))
    print("Output:", min_operations(nums, x))


if __name__ == "__main__":
    main()
