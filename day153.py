# day153.py
# LeetCode 1807 - Evaluate the Bracket Pairs of a String

def evaluate(s, knowledge):
    values = {key: value for key, value in knowledge}

    result = []
    i = 0

    while i < len(s):
        if s[i] == '(':
            j = i + 1

            while s[j] != ')':
                j += 1

            key = s[i + 1:j]
            result.append(values.get(key, '?'))

            i = j + 1
        else:
            result.append(s[i])
            i += 1

    return ''.join(result)


# User Input
s = input("Enter the string: ")

n = int(input("Enter number of knowledge pairs: "))

knowledge = []
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    knowledge.append([key, value])

# Output
print("Result:", evaluate(s, knowledge))
