from collections import Counter

def lex_palindromic_permutation(s, target):
    n = len(s)
    freq = Counter(s)

    # A palindrome can have at most one character with odd frequency.
    odd = [ch for ch in freq if freq[ch] % 2]
    if len(odd) > 1:
        return ""

    half = []
    for ch in sorted(freq):
        half.extend([ch] * (freq[ch] // 2))

    middle = odd[0] if n % 2 else ""

    def build(left):
        return ''.join(left) + middle + ''.join(left[::-1])

    # Find the lexicographically smallest half whose palindrome > target.
    # Try every possible position where the first half becomes larger.
    for i in range(n // 2 - 1, -1, -1):
        used = Counter(half[:i])
        available = Counter(half[i:])

        target_ch = target[i]

        # Keep the prefix equal to target.
        # If prefix cannot be formed, this position cannot be used.
        if any(used[ch] > half.count(ch) for ch in used):
            continue

        for ch in sorted(available):
            if ch > target_ch:
                available[ch] -= 1
                if available[ch] == 0:
                    del available[ch]

                result_half = list(target[:i]) + [ch]

                for c in sorted(available):
                    result_half.extend([c] * available[c])

                if len(result_half) == n // 2:
                    return build(result_half)

    # Check if target's first half itself forms a palindrome greater than target.
    target_half = list(target[:n // 2])
    needed = Counter(target_half)

    if all(needed[ch] <= freq[ch] // 2 for ch in needed):
        candidate = build(target_half)
        if candidate > target:
            return candidate

    return ""


# User input
s = input("Enter s: ").strip()
target = input("Enter target: ").strip()

print(lex_palindromic_permutation(s, target))
