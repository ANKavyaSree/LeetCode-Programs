n = int(input("Enter a positive integer: "))

digits = list(map(int, str(n)))

first = second = 0

for digit in digits:
    if digit > first:
        second = first
        first = digit
    elif digit > second:
        second = digit

result = first * second

print("Maximum product of two digits:", result)
