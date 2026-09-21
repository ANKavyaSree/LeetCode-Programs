# day148.py

def find_x_value(nums, k):
    # dp[r] = number of subarrays ending at the previous index
    # whose product % k == r
    dp = [0] * k
    result = [0] * k

    for num in nums:
        value = num % k
        new_dp = [0] * k

        # Start a new subarray with nums[i]
        new_dp[value] += 1

        # Extend every subarray ending at the previous index
        for r in range(k):
            if dp[r]:
                new_r = (r * value) % k
                new_dp[new_r] += dp[r]

        dp = new_dp

        # Every non-empty subarray corresponds to exactly one
        # possible remaining array after removing a prefix and suffix.
        for r in range(k):
            result[r] += dp[r]

    return result


def main():
    nums = list(map(int, input("Enter nums: ").split()))
    k = int(input("Enter k: "))

    answer = find_x_value(nums, k)
    print("Output:", answer)


if __name__ == "__main__":
    main()
