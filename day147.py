# LeetCode 3498 - Reverse Degree of a String
# Day 147 - User Input Version

s = input("Enter the string: ")

total = 0

for i, ch in enumerate(s, 1):
    reverse_value = 26 - (ord(ch) - ord('a'))
    total += reverse_value * i

print(total)
