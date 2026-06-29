n = int(input("Enter number of patterns: "))

patterns = []

print("Enter patterns:")
for _ in range(n):
    patterns.append(input())

word = input("Enter word: ")

count = 0

for pattern in patterns:
    if pattern in word:
        count += 1

print("Number of matching patterns:", count)


# sample input
# Enter number of patterns: 4
# Enter patterns:
# a
# abc
# bc
# d
# Enter word: abc

# sample output
# Number of matching patterns: 3