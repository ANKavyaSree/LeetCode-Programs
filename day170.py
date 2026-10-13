# day170.py
# LeetCode 3727 - Maximum Alternating Sum of Squares
# User-input program

def max_alternating_sum(nums):
    squares = sorted((x * x for x in nums), reverse=True)
    half = (len(nums) + 1) // 2
    return sum(squares[:half]) - sum(squares[half:])


def main():
    # Enter integers separated by spaces, e.g. 1 2 3
    nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
    print("Maximum alternating sum of squares:", max_alternating_sum(nums))


if __name__ == "__main__":
    main()
