def maximumSaleItems(items, budget):
    n = len(items)
    min_price = min(price for factor, price in items)

    values = []
    for i in range(n):
        factor = items[i][0]
        bonus = sum(
            1 for j in range(n)
            if i != j and items[j][0] % factor == 0
        )
        values.append(1 + bonus)

    dp = [-1] * (budget + 1)
    dp[0] = 0

    for i in range(n):
        price = items[i][1]
        value = values[i]

        for b in range(budget, price - 1, -1):
            if dp[b - price] != -1:
                dp[b] = max(dp[b], dp[b - price] + value)

    ans = 0
    for spent in range(budget + 1):
        if dp[spent] != -1:
            ans = max(ans, dp[spent] + (budget - spent) // min_price)

    return ans


if __name__ == "__main__":
    n = int(input())
    items = []
    for _ in range(n):
        factor, price = map(int, input().split())
        items.append([factor, price])

    budget = int(input())
    print(maximumSaleItems(items, budget))
