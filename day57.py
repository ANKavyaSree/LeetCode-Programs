def max_ice_cream(costs, coins):
    costs.sort()

    count = 0

    for cost in costs:
        if coins >= cost:
            coins -= cost
            count += 1
        else:
            break

    return count


# User Input Section
n = int(input("Enter number of ice cream bars: "))

print("Enter the costs of ice cream bars:")
costs = list(map(int, input().split()))

coins = int(input("Enter available coins: "))

result = max_ice_cream(costs, coins)

print("Maximum ice cream bars that can be bought:", result)


# sample input
# Enter number of ice cream bars: 5
# Enter the costs of ice cream bars:
# 1 3 2 4 1
# Enter available coins: 7

# sample output
# Maximum ice cream bars that can be bought: 4