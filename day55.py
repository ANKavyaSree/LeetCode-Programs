def largest_altitude(gain):
    altitude = 0
    max_altitude = 0

    for g in gain:
        altitude += g
        max_altitude = max(max_altitude, altitude)

    return max_altitude


# User Input
n = int(input("Enter number of altitude gains: "))

print("Enter the gain values:")
gain = list(map(int, input().split()))

if len(gain) != n:
    print("Error: Number of gains entered does not match n.")
else:
    print("Highest Altitude:", largest_altitude(gain))


# sample input
# Enter number of altitude gains: 5
# Enter the gain values:
# -5 1 5 0 -7

# sample output
# Highest Altitude: 1