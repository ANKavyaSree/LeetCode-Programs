# Day 191 - Minimum Moves to Make All Elements Equal
# User input program

nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

maximum = max(nums)
moves = 0

for num in nums:
    moves += maximum - num

print(moves)
