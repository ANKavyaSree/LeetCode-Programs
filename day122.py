def shortest_beautiful_substring(s, k):
    ones = [i for i, ch in enumerate(s) if ch == '1']

    if len(ones) < k:
        return ""

    best = ""

    for i in range(len(ones) - k + 1):
        left = ones[i]
        right = ones[i + k - 1]
        candidate = s[left:right + 1]

        if not best or len(candidate) < len(best):
            best = candidate
        elif len(candidate) == len(best) and candidate < best:
            best = candidate

    return best


s = input("Enter binary string: ").strip()
k = int(input("Enter k: "))

print(shortest_beautiful_substring(s, k))
