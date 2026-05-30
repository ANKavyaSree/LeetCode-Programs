# Day 35 - Block Placement Queries
# User Input Version (Simulation Approach)

obstacles = set()

q = int(input("Enter number of queries: "))

results = []

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # Type 1: Place obstacle
        x = query[1]
        obstacles.add(x)

    else:
        # Type 2: Check block placement
        x, sz = query[1], query[2]

        can_place = False

        for start in range(0, x - sz + 2):
            end = start + sz

            valid = True

            for obs in obstacles:
                if start < obs < end:
                    valid = False
                    break

            if valid and end <= x:
                can_place = True
                break

        results.append(can_place)

print("Result:", results)


# sample input
# Enter number of queries: 4
# 1 2
# 2 3 3
# 2 3 1
# 2 2 2

# sample output
# Result: [False, True, True]