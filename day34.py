# Day 34 - Minimum Element After Replacement With Digit Sum
# User Input Version

def digit_sum(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total


n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter array elements: ").split()))

replaced = []

for num in nums:
    replaced.append(digit_sum(num))

print("Array after replacement:", replaced)
print("Minimum element:", min(replaced))

# sample input
# Enter number of elements: 4
# Enter array elements: 10 12 13 14

# sample output
# Array after replacement: [1, 3, 4, 5]
# Minimum element: 1