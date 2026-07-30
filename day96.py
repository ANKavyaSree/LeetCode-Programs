word = input("Enter the word: ")

n = len(word)
pushes = 0

for i in range(n):
    pushes += i // 8 + 1

print("Minimum number of pushes:", pushes)
