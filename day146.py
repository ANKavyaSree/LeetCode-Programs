# Circle and Rectangle Overlap
# LeetCode 1401 - User Input Version

radius, xCenter, yCenter = map(int, input("Enter radius xCenter yCenter: ").split())
x1, y1, x2, y2 = map(int, input("Enter x1 y1 x2 y2: ").split())

# Find the closest point in the rectangle to the circle center
closest_x = max(x1, min(xCenter, x2))
closest_y = max(y1, min(yCenter, y2))

# Check whether the closest point lies inside/on the circle
distance_squared = (closest_x - xCenter) ** 2 + (closest_y - yCenter) ** 2

if distance_squared <= radius ** 2:
    print("true")
else:
    print("false")
