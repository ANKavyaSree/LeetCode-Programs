def separateDigits(nums):
    result = []

    for num in nums:
        digits = str(num)   # Convert number to string
        for digit in digits:
            result.append(int(digit))

    return result


# User Input
nums = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
answer = separateDigits(nums)

# Output
print("Separated Digits:", answer)


# sample input
# Enter array elements separated by space: 13 25 83 77
# sample output
# Separated Digits: [1, 3, 2, 5, 8, 3, 7, 7]