class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        count = {}

        for i in range(len(nums) - k + 1):
            window = set(nums[i:i + k])

            for num in window:
                count[num] = count.get(num, 0) + 1

        answer = -1

        for num, frequency in count.items():
            if frequency == 1:
                answer = max(answer, num)

        return answer


# User Input
nums = list(map(
    int,
    input("Enter array elements separated by spaces: ").split()
))

k = int(input("Enter k: "))

solution = Solution()
result = solution.largestInteger(nums, k)

print("Largest almost missing integer:", result)
