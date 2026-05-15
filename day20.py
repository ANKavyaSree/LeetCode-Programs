def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Minimum element is in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Minimum is at mid or left half
            right = mid

    return nums[left]


# User Input
n = int(input("Enter size of array: "))
nums = list(map(int, input("Enter rotated sorted array elements: ").split()))

# Output
print("Minimum element in array:", findMin(nums))

# sample input
# Enter size of array: 5
# Enter rotated sorted array elements: 3 4 5 1 2

# sample output
# Minimum element in array: 1