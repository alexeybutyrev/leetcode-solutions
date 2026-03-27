# Problem: Partition Equal Subset Sum
# Language: python3
# Runtime: 1164 ms
# Memory: 14.3 MB

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if (S & 1) != 0:
            return False
        
        S >>= 1
        
        dp = [False] * (S + 1) 
        dp[0] = True
        for n in nums:
            for j in range(S, n - 1, -1):
                dp[j] |= dp[j - n]

        return dp[S]