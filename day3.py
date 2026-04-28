# Minimum Operations to Make a Uni-Value Grid
# Median + Greedy Approach

def minOperations(grid, x):
    nums = []

    # Flatten grid
    for row in grid:
        for num in row:
            nums.append(num)

    # Check if making uni-value is possible
    remainder = nums[0] % x
    for num in nums:
        if num % x != remainder:
            return -1

    # Median minimizes operations
    nums.sort()
    target = nums[len(nums)//2]

    operations = 0
    for num in nums:
        operations += abs(num - target) // x

    return operations


# -------- User Input --------
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
x = int(input("Enter value of x: "))

print("Enter grid rows (space-separated integers):")
grid=[]

for i in range(rows):
    row=list(map(int,input().split()))
    grid.append(row)

print(minOperations(grid,x))


##Sample input
# Enter number of rows: 2
# Enter number of columns: 2
# Enter value of x: 2
# 2 4
# 6 8

##Sample Output
#4