s = input("Enter the string: ")
k = int(input("Enter the value of k: "))

while len(s) > k:
    result = ""

    for i in range(0, len(s), k):
        group = s[i:i + k]
        total = sum(int(ch) for ch in group)
        result += str(total)

    s = result

print("Final string:", s)
