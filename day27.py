def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Target found
        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:

            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# User Input
n = int(input("Enter size of array: "))
nums = list(map(int, input("Enter rotated sorted array elements: ").split()))
target = int(input("Enter target element: "))

# Output
result = search(nums, target)

if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found")

# sample input
# Enter size of array: 7
# Enter rotated sorted array elements: 4 5 6 7 0 1 2
# Enter target element: 0


# sample output
# Target found at index: 4