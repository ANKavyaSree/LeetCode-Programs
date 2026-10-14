# day171.py
# Maximum score good integer

def maxSumOfSquares(num: int, digit_sum: int) -> str:
    if digit_sum > 9 * num:
        return ""

    result = []
    for _ in range(num):
        digit = min(9, digit_sum)
        result.append(str(digit))
        digit_sum -= digit

    return "".join(result)


if __name__ == "__main__":
    num = int(input("Enter num: "))
    digit_sum = int(input("Enter sum: "))
    print(maxSumOfSquares(num, digit_sum))
