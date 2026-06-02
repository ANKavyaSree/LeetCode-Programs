def earliest_finish_time(land_start, land_duration, water_start, water_duration):
    ans = float('inf')

    # Land ride first, then Water ride
    for i in range(len(land_start)):
        land_finish = land_start[i] + land_duration[i]

        for j in range(len(water_start)):
            start_water = max(land_finish, water_start[j])
            finish_time = start_water + water_duration[j]

            ans = min(ans, finish_time)

    # Water ride first, then Land ride
    for j in range(len(water_start)):
        water_finish = water_start[j] + water_duration[j]

        for i in range(len(land_start)):
            start_land = max(water_finish, land_start[i])
            finish_time = start_land + land_duration[i]

            ans = min(ans, finish_time)

    return ans


# User Input
n = int(input("Enter number of land rides: "))

print("Enter land ride start times:")
land_start = list(map(int, input().split()))

print("Enter land ride durations:")
land_duration = list(map(int, input().split()))

m = int(input("Enter number of water rides: "))

print("Enter water ride start times:")
water_start = list(map(int, input().split()))

print("Enter water ride durations:")
water_duration = list(map(int, input().split()))

result = earliest_finish_time(
    land_start,
    land_duration,
    water_start,
    water_duration
)

print("Earliest Finish Time:", result)


# sample input
# Enter number of land rides: 2
# Enter land ride start times:
# 2 8
# Enter land ride durations:
# 4 1
# Enter number of water rides: 1
# Enter water ride start times:
# 6
# Enter water ride durations:
# 3

# sample output
# Earliest Finish Time: 9
