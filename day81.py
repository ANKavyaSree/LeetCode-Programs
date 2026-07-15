def gcdOfSums(n: int) -> int:
    return n

if __name__ == "__main__":
    print("--- GCD of Odd and Even Sums ---")
    try:
        n = int(input("Enter an integer n: ").strip())
        if n < 1:
            print("Please enter a positive integer greater than or equal to 1.")
        else:
            # Let's show the breakdown manually to prove it
            sum_odd = n * n
            sum_even = n * (n + 1)
            
            print(f"\nSum of first {n} odd numbers (sumOdd): {sum_odd}")
            print(f"Sum of first {n} even numbers (sumEven): {sum_even}")
            print(f"Output: {gcdOfSums(n)}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# sample input
# Enter an integer n: 4

# sample output
# Sum of first 4 odd numbers (sumOdd): 16
# Sum of first 4 even numbers (sumEven): 20
# Output: 4