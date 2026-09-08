class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp[i] = number of distinct subsequences including the empty one
        # after processing the first i characters.
        dp = 1

        # last[c] stores the dp value before the previous occurrence
        # of character c.
        last = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')

            new_dp = (2 * dp - last[idx]) % MOD
            last[idx] = dp
            dp = new_dp

        # Remove the empty subsequence.
        return (dp - 1) % MOD


# User input
s = input("Enter string: ")

solution = Solution()
result = solution.distinctSubseqII(s)

print("Number of distinct non-empty subsequences:", result)
