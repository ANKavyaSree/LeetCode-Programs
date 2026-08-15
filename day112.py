class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0

        for num in nums:
            total_xor ^= num

        if total_xor != 0:
            return len(nums)

        for num in nums:
            if num != 0:
                return len(nums) - 1

        return 0


# User Input
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

solution = Solution()
result = solution.longestSubsequence(nums)

print("Longest subsequence length:", result)
