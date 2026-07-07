n = int(input())

digits = []

for ch in str(n):
    if ch != '0':
        digits.append(ch)

if digits:
    x = int("".join(digits))
else:
    x = 0

digit_sum = 0

for d in digits:
    digit_sum += int(d)

print(x * digit_sum)

# sample input
# 10203004

# sample output
# 12340