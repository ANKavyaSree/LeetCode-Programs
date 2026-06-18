def angle_clock(hour, minutes):
    # Position of hour hand
    hour_angle = (hour % 12) * 30 + minutes * 0.5

    # Position of minute hand
    minute_angle = minutes * 6

    # Difference between angles
    angle = abs(hour_angle - minute_angle)

    # Return smaller angle
    return min(angle, 360 - angle)


# User Input
hour = int(input("Enter hour (1-12): "))
minutes = int(input("Enter minutes (0-59): "))

result = angle_clock(hour, minutes)

print("Smaller angle between clock hands:", result)


# sample input
# Enter hour (1-12): 3
# Enter minutes (0-59): 15

# sample output
# Smaller angle between clock hands: 7.5
