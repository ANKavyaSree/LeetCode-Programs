def sequentialDigits(low: int, high: int) -> list[int]:
    digits = "123456789"
    result = []
    for length in range(2, 10):
        for start in range(10 - length):
            num = int(digits[start : start + length])
            if low <= num <= high:
                result.append(num)
    return result

if __name__ == "__main__":
    print("--- Sequential Digits Generator ---")
    try:
        low = int(input("Enter low limit: ").strip())
        high = int(input("Enter high limit: ").strip())
        
        if low > high:
            print("Error: low limit cannot be greater than high limit.")
        else:
            output = sequentialDigits(low, high)
            print(f"Sequential digits in range [{low}, {high}]: {output}")
            
    except ValueError:
        print("Invalid input. Please enter valid integers.")


# sample input
# Enter low limit: 1000
# Enter high limit: 13000

# sample output
# Sequential digits in range [1000, 13000]: [1234, 2345, 3456, 4567, 5678, 6789, 12345]