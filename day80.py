from math import gcd
from functools import lru_cache

def countPairsOfSubsequences(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    
    @lru_cache(None)
    def dp(idx, g1, g2):
        if idx == n:
            return 1 if g1 == g2 and g1 > 0 else 0
        
        res = dp(idx + 1, g1, g2)
        
        new_g1 = nums[idx] if g1 == 0 else gcd(g1, nums[idx])
        res = (res + dp(idx + 1, new_g1, g2)) % MOD
        
        new_g2 = nums[idx] if g2 == 0 else gcd(g2, nums[idx])
        res = (res + dp(idx + 1, g1, new_g2)) % MOD
        
        return res

    return dp(0, 0, 0)

if __name__ == "__main__":
    print("--- Equal GCD Disjoint Subsequence Pair Counter ---")
    try:
        user_input = input("Enter space-separated integers (e.g., 10 20 30): ").strip()
        if not user_input:
            print("Array cannot be empty.")
        else:
            nums = list(map(int, user_input.split()))
            if len(nums) > 200 or any(x > 200 or x < 1 for x in nums):
                print("Warning: Input breaks problem constraints (1 <= entry, length <= 200).")
            
            result = countPairsOfSubsequences(nums)
            print(f"Total matching subsequence pairs: {result}")
    except ValueError:
        print("Invalid syntax. Please supply space-separated numeric integers.")


# sample input
# Enter space-separated integers (e.g., 10 20 30): 10 20 30

# sample output
# Total matching subsequence pairs: 2
