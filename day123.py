def lex_greater_permutation(s, target):
    n = len(s)
    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    prefix = []

    for i in range(n):
        t = ord(target[i]) - ord('a')

        if count[t] > 0:
            count[t] -= 1
            prefix.append(target[i])
        else:
            for c in range(t + 1, 26):
                if count[c] > 0:
                    count[c] -= 1
                    result = ''.join(prefix) + chr(c + ord('a'))
                    for j in range(26):
                        result += chr(j + ord('a')) * count[j]
                    return result
            break

    for i in range(len(prefix) - 1, -1, -1):
        c = ord(prefix[i]) - ord('a')
        count[c] += 1
        prefix.pop()

        for bigger in range(c + 1, 26):
            if count[bigger] > 0:
                count[bigger] -= 1
                result = ''.join(prefix) + chr(bigger + ord('a'))
                for j in range(26):
                    result += chr(j + ord('a')) * count[j]
                return result

    return ""


s = input("Enter s: ").strip()
target = input("Enter target: ").strip()

print(lex_greater_permutation(s, target))
