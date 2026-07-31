from collections import Counter

word = input("Enter the word: ")

freq = sorted(Counter(word).values(), reverse=True)

pushes = 0

for i, count in enumerate(freq):
    pushes += count * (i // 8 + 1)

print("Minimum number of pushes:", pushes)
