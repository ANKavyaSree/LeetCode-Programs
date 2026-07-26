def maximumProduct(nums: list[int]) -> int:
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    
    for n in nums:
        if n > max1:
            max3 = max2; max2 = max1; max1 = n
        elif n > max2:
            max3 = max2; max2 = n
        elif n > max3:
            max3 = n
            
        if n < min1:
            min2 = min1; min1 = n
        elif n < min2:
            min2 = n
            
    return max(max1 * max2 * max3, min1 * min2 * max1)

if __name__ == "__main__":
    print("--- Maximum Product of Three Numbers Counter ---")
    try:
        user_input = input("Enter space-separated integers (e.g., -10 -10 1 2 3): ").strip()
        if not user_input:
            print("Array cannot be empty.")
        else:
            nums = list(map(int, user_input.split()))
            if len(nums) < 3:
                print("Error: Please provide at least 3 integers.")
            else:
                result = maximumProduct(nums)
                print(f"Maximum Product: {result}")
    except ValueError:
        print("Invalid syntax. Please enter numeric integers only.")

# sample input
# Enter space-separated integers (e.g., -10 -10 1 2 3): -10 -10 1 2 3

# sample output
# Maximum Product: 300
