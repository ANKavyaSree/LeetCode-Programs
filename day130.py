class Solution:
    def uniformArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        if min_odd != float('inf'):
            for x in nums1:
                if x % 2 == 0 and min_odd >= x:
                    break
            else:
                return True

        if min_even != float('inf'):
            for x in nums1:
                if x % 2 == 1 and min_even >= x:
                    break
            else:
                return True

        if min_odd == float('inf') or min_even == float('inf'):
            return True

        return False


nums1 = list(map(int, input("Enter nums1 separated by spaces: ").split()))

solution = Solution()
print(solution.uniformArray(nums1))
