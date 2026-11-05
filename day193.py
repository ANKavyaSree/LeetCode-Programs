# Day 193 - Find the Distance Value Between Two Arrays

def findTheDistanceValue(arr1, arr2, d):
    count = 0

    for x in arr1:
        valid = True

        for y in arr2:
            if abs(x - y) <= d:
                valid = False
                break

        if valid:
            count += 1

    return count


# User input
arr1 = list(map(int, input("Enter elements of arr1: ").split()))
arr2 = list(map(int, input("Enter elements of arr2: ").split()))
d = int(input("Enter d: "))

result = findTheDistanceValue(arr1, arr2, d)
print("Distance value:", result)
