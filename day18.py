def minMoves(nums, limit):
    n = len(nums)
    diff = [0] * (2 * limit + 2)

    for i in range(n // 2):
        a = nums[i]
        b = nums[n - 1 - i]

        low = 1 + min(a, b)
        high = limit + max(a, b)
        s = a + b

        diff[2] += 2
        diff[low] -= 1
        diff[s] -= 1
        diff[s + 1] += 1
        diff[high + 1] += 1

    moves = float('inf')
    current = 0

    for x in range(2, 2 * limit + 1):
        current += diff[x]
        moves = min(moves, current)

    return moves


# User Input Section
n = int(input("Enter size of array (even number): "))
nums = list(map(int, input("Enter array elements: ").split()))
limit = int(input("Enter limit: "))

# Output
print("Minimum Moves Required:", minMoves(nums, limit))


# sample input
# Enter size of array (even number): 4
# Enter array elements: 1 2 4 3
# Enter limit: 4

# sample output
# Minimum Moves Required: 1