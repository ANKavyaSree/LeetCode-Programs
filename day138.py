class Solution:
    def totalNumbers(self, digits):
        numbers = set()

        n = len(digits)

        for i in range(n):
            # Hundreds digit cannot be 0
            if digits[i] == 0:
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    # Last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    numbers.add(number)

        return len(numbers)


# User input
digits = list(map(int, input("Enter the digits separated by spaces: ").split()))

solution = Solution()
result = solution.totalNumbers(digits)

print("Number of distinct 3-digit even numbers:", result)
