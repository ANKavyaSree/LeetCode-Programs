def waviness(num):
    s = str(num)

    if len(s) < 3:
        return 0

    count = 0

    for i in range(1, len(s) - 1):
        if s[i] > s[i - 1] and s[i] > s[i + 1]:
            count += 1
        elif s[i] < s[i - 1] and s[i] < s[i + 1]:
            count += 1

    return count


def total_waviness(num1, num2):
    total = 0

    for num in range(num1, num2 + 1):
        total += waviness(num)

    return total


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

result = total_waviness(num1, num2)

print("Total Waviness:", result)



# sample input
# Enter num1: 120
# Enter num2: 130

# sample output
# Total Waviness: 3
