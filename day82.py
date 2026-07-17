import bisect

def gcdValues(nums: list[int], queries: list[int]) -> list[int]:
    max_val = max(nums)
    freq = [0] * (max_val + 1)
    for num in nums:
        freq[num] += 1
        
    exact_gcd_counts = [0] * (max_val + 1)
    for g in range(max_val, 0, -1):
        multiples_count = 0
        for multiple in range(g, max_val + 1, g):
            multiples_count += freq[multiple]
        
        total_pairs = (multiples_count * (multiples_count - 1)) // 2
        subtracted_pairs = 0
        for multiple in range(2 * g, max_val + 1, g):
            subtracted_pairs += exact_gcd_counts[multiple]
            
        exact_gcd_counts[g] = total_pairs - subtracted_pairs
        
    prefix_sums = []
    current_running_sum = 0
    for g in range(1, max_val + 1):
        if exact_gcd_counts[g] > 0:
            current_running_sum += exact_gcd_counts[g]
            prefix_sums.append((current_running_sum, g))
            
    ans = []
    for q in queries:
        idx = bisect.bisect_right(prefix_sums, (q, float('inf')))
        ans.append(prefix_sums[idx][1])
    return ans

if __name__ == "__main__":
    print("--- Sorted GCD Pair Queries Simulator ---")
    try:
        nums_in = input("Enter space-separated array integers (nums): ").strip()
        queries_in = input("Enter space-separated query indices (queries): ").strip()
        
        nums = list(map(int, nums_in.split()))
        queries = list(map(int, queries_in.split()))
        
        output = gcdValues(nums, queries)
        print(f"\nResulting Answers: {output}")
    except (ValueError, IndexError):
        print("Invalid array formatting or indexes out of bounds.")

# sample input
# Enter space-separated array integers (nums): 2 3 4
# Enter space-separated query indices (queries): 0 2 2

# sample output
# Resulting Answers: [1, 2, 2]
