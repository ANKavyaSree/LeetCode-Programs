def max_building(n, restrictions):
    restrictions.append([1, 0])

    if restrictions[-1][0] != n:
        restrictions.append([n, n - 1])

    restrictions.sort()

    m = len(restrictions)

    # Left to Right
    for i in range(1, m):
        restrictions[i][1] = min(
            restrictions[i][1],
            restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0]
        )

    # Right to Left
    for i in range(m - 2, -1, -1):
        restrictions[i][1] = min(
            restrictions[i][1],
            restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0]
        )

    ans = 0

    for i in range(1, m):
        x1, h1 = restrictions[i - 1]
        x2, h2 = restrictions[i]

        dist = x2 - x1
        peak = (h1 + h2 + dist) // 2

        ans = max(ans, peak)

    return ans


# User Input
n = int(input("Enter number of buildings: "))

m = int(input("Enter number of restrictions: "))

restrictions = []

print("Enter restrictions (id maxHeight):")
for _ in range(m):
    building_id, max_height = map(int, input().split())
    restrictions.append([building_id, max_height])

print("Maximum possible building height:", max_building(n, restrictions))


# sample input
# Enter number of buildings: 5
# Enter number of restrictions: 2
# Enter restrictions (id maxHeight):
# 2 1
# 4 1

# sample output
# Maximum possible building height: 2