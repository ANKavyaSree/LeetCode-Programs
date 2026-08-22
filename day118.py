# Day 118 - Check Divisibility by Digit Sum and Product

n = int(input("Enter a positive integer: "))

temp = n
digit_sum = 0
digit_product = 1

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    digit_product *= digit
    temp //= 10

total = digit_sum + digit_product

if n % total == 0:
    print(True)
else:
    print(False)
