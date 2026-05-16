def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1

        elif nums[mid] < nums[right]:
            right = mid

        else:
            # When duplicates exist
            right -= 1

    return nums[left]


# User Input
n = int(input("Enter size of array: "))
nums = list(map(int, input("Enter rotated sorted array elements: ").split()))

# Output
print("Minimum element in array:", findMin(nums))


# sample input
# Enter size of array: 5
# Enter rotated sorted array elements: 2 2 2 0 1

# sample output
# Minimum element in array: 0