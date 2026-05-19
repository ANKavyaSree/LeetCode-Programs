def getCommon(nums1, nums2):
    i = 0
    j = 0

    # Two Pointer Approach
    while i < len(nums1) and j < len(nums2):

        if nums1[i] == nums2[j]:
            return nums1[i]

        elif nums1[i] < nums2[j]:
            i += 1

        else:
            j += 1

    return -1


# User Input
n1 = int(input("Enter size of first array: "))
nums1 = list(map(int, input("Enter elements of first sorted array: ").split()))

n2 = int(input("Enter size of second array: "))
nums2 = list(map(int, input("Enter elements of second sorted array: ").split()))

# Output
print("Minimum Common Value:", getCommon(nums1, nums2))


# sample input
# Enter size of first array: 3
# Enter elements of first sorted array: 1 2 3
# Enter size of second array: 2
# Enter elements of second sorted array: 2 4

# sample output
# Minimum Common Value: 2
