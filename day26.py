def longestCommonPrefix(arr1, arr2):

    prefixes = set()

    # Store all prefixes from arr1
    for num in arr1:
        num = str(num)

        for i in range(1, len(num) + 1):
            prefixes.add(num[:i])

    longest = 0

    # Check prefixes in arr2
    for num in arr2:
        num = str(num)

        for i in range(1, len(num) + 1):
            if num[:i] in prefixes:
                longest = max(longest, i)

    return longest


# User Input
n1 = int(input("Enter size of first array: "))
arr1 = list(map(int, input("Enter elements of first array: ").split()))

n2 = int(input("Enter size of second array: "))
arr2 = list(map(int, input("Enter elements of second array: ").split()))

# Output
print("Length of Longest Common Prefix:", longestCommonPrefix(arr1, arr2))


# sample input
# Enter size of first array: 3
# Enter elements of first array: 1 10 100
# Enter size of second array: 1
# Enter elements of second array: 1000

# sample output
# Length of Longest Common Prefix: 3