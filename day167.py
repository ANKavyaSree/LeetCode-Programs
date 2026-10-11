class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        n = len(diff)
        diff.append(0)

        for i in range(n):
            count = i + 1
            cost = count * (diff[i] - diff[i + 1])

            if cost <= k:
                k -= cost
            else:
                level = diff[i] - k // count
                remainder = k % count

                ans = remainder * (level - 1) ** 2
                ans += (count - remainder) * level ** 2

                for j in range(i + 1, n):
                    ans += diff[j] ** 2

                return ans

        return 0


if __name__ == "__main__":
    nums1 = list(map(int, input("Enter nums1 elements separated by spaces: ").split()))
    nums2 = list(map(int, input("Enter nums2 elements separated by spaces: ").split()))
    k1 = int(input("Enter k1: "))
    k2 = int(input("Enter k2: "))

    solution = Solution()
    print("Minimum sum of squared difference:", solution.minSumSquareDiff(nums1, nums2, k1, k2))
