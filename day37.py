def minimum_cost(cost):
    # Sort in descending order
    cost.sort(reverse=True)

    total_cost = 0

    for i in range(len(cost)):
        # Every 3rd candy is free
        if (i + 1) % 3 != 0:
            total_cost += cost[i]

    return total_cost


# User Input
n = int(input("Enter number of candies: "))

print("Enter candy costs:")
cost = list(map(int, input().split()))

result = minimum_cost(cost)

print("Minimum Cost:", result)

# sample input
# Enter number of candies: 3
# Enter candy costs:
# 1 2 3

# sample output
# Minimum Cost: 5
