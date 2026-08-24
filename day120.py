def stone_game_viii(stones):
    n = len(stones)

    total = sum(stones)
    best = total

    for i in range(n - 2, 0, -1):
        total -= stones[i + 1]
        best = max(best, total - best)

    return best


# User input
stones = list(map(int, input("Enter stones separated by spaces: ").split()))

print(stone_game_viii(stones))
