# Problem: Combination Sum IV
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)
        
        for n in nums:
            if n <= target:
                dp[n] = 1
            
        for t in range(1, target+1):
            for n in nums:
                if n <= t:
                    dp[t] += dp[t-n]
        
        return dp[target]