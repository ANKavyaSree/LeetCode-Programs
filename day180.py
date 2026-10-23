# day180.py
# Maximum K to Sort a Permutation

def sort_permutation(nums):
    ans = -1

    for i, num in enumerate(nums):
        if num != i:
            ans &= num

    return max(ans, 0)


if __name__ == "__main__":
    # Example input: [0, 3, 2, 1]
    raw = input("Enter permutation elements separated by spaces: ").strip()
    nums = list(map(int, raw.split()))

    print(sort_permutation(nums))
