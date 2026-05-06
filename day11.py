def rotateTheBox(box):
    m, n = len(box), len(box[0])

    # Step 1: Apply gravity (stones fall to the right)
    for row in box:
        empty = n - 1
        for col in range(n - 1, -1, -1):
            if row[col] == '*':
                empty = col - 1
            elif row[col] == '#':
                row[col], row[empty] = '.', '#'
                empty -= 1

    # Step 2: Rotate 90 degrees clockwise
    result = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m - 1 - i] = box[i][j]

    return result


# -------- User Input --------
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter the box row by row (use #, *, .):")
box = []
for _ in range(m):
    row = list(input().strip())
    box.append(row)

rotated = rotateTheBox(box)

print("\nRotated Box:")
for row in rotated:
    print("".join(row))

# sample input 
# Enter number of rows: 2
# Enter number of columns: 3
# Enter the box row by row:
# #.*
# ##.
 
# sample output
# Rotated Box:
# .#
# ##
# *.