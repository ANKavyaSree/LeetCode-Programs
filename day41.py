def waviness(num):
    digits = str(num)

    if len(digits) < 3:
        return 0

    count = 0

    for i in range(1, len(digits) - 1):
        if (digits[i] > digits[i - 1] and digits[i] > digits[i + 1]) or \
           (digits[i] < digits[i - 1] and digits[i] < digits[i + 1]):
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