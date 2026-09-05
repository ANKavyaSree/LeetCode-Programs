class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            if prefix_max - suffix_min[i] <= k:
                return i

        return -1


nums = list(map(int, input("Enter nums separated by spaces: ").split()))
k = int(input("Enter k: "))

solution = Solution()
print(solution.firstStableIndex(nums, k))
