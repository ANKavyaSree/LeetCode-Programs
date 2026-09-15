def rectangle_overlap(rec1, rec2):
    # Find the width and height of the intersection.
    overlap_width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
    overlap_height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])

    return overlap_width > 0 and overlap_height > 0


# User input
rec1 = list(map(int, input("Enter rec1 (4 integers): ").split()))
rec2 = list(map(int, input("Enter rec2 (4 integers): ").split()))

print(rectangle_overlap(rec1, rec2))
