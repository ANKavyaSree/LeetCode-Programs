class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt = [0, 0, 0]

        for stone in stones:
            cnt[stone % 3] += 1

        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        return abs(cnt[1] - cnt[2]) > 2


# User Input
stones = list(map(
    int,
    input("Enter stone values separated by spaces: ").split()
))

solution = Solution()
result = solution.stoneGameIX(stones)

print("Alice wins:", result)
