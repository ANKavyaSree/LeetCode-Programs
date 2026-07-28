from collections import Counter

s = input("Enter a palindromic string: ")

freq = Counter(s)

left = []
middle = ""

for ch in sorted(freq):
    left.append(ch * (freq[ch] // 2))
    if freq[ch] % 2:
        middle = ch

left = "".join(left)
result = left + middle + left[::-1]

print("Lexicographically smallest palindromic permutation:", result)
