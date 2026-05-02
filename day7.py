def isGood(num):
    valid = {0:0, 1:1, 8:8, 2:5, 5:2, 6:9, 9:6}
    changed = False

    for d in map(int, str(num)):
        if d not in valid:
            return False
        if valid[d] != d:
            changed = True

    return changed


def rotatedDigits(n):
    count = 0
    for i in range(1, n+1):
        if isGood(i):
            count += 1
    return count


# -------- User Input --------
n = int(input("Enter n: "))
print("Count of good numbers:", rotatedDigits(n))

#sample input
# Enter n: 10


#sample output
#Count of good numbers: 4