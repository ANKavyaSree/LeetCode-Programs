def arrayRankTransform(arr: list[int]) -> list[int]:
    sorted_unique = sorted(list(set(arr)))
    rank_map = {num: i + 1 for i, num in enumerate(sorted_unique)}
    return [rank_map[num] for num in arr]

if __name__ == "__main__":
    print("--- Array Rank Transformer ---")
    try:
        # Accept input as a space-separated string
        user_input = input("Enter space-separated integers (e.g., 37 12 28 9): ").strip()
        
        if not user_input:
            arr = []
        else:
            arr = list(map(int, user_input.split()))
            
        # Compute and print ranks
        output_ranks = arrayRankTransform(arr)
        print(f"Original Array: {arr}")
        print(f"Ranked Output:  {output_ranks}")
        
    except ValueError:
        print("Invalid input format. Please enter numbers only.")


# sample input
# Enter space-separated integers (e.g., 37 12 28 9): 37 12 28 9 100 56 80 5 12

# sample output
# Original Array: [37, 12, 28, 9, 100, 56, 80, 5, 12]
# Ranked Output:  [5, 3, 4, 2, 8, 6, 7, 1, 3]
