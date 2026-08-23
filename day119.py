def sum_game(num: str) -> bool:
    n = len(num)
    diff = 0
    left_q = 0
    right_q = 0

    for i in range(n // 2):
        if num[i] == '?':
            left_q += 1
        else:
            diff += int(num[i])

    for i in range(n // 2, n):
        if num[i] == '?':
            right_q += 1
        else:
            diff -= int(num[i])

    # Odd number of '?' means Alice can force a win.
    if (left_q + right_q) % 2 == 1:
        return True

    # Bob wins only when the difference can be exactly balanced.
    return 2 * diff != 9 * (right_q - left_q)


# User input
num = input("Enter num: ").strip()

print(sum_game(num))
