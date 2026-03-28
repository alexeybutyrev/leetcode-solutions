# Problem: Wiggle Subsequence
# Language: python3
# Runtime: 32 ms
# Memory: 14.1 MB

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1
                
        P = []
        for i in range(1, N):
            if nums[i] != nums[i-1]:
                P.append(nums[i] - nums[i-1])
        
        if not P:
            return 1
        
        M = len(P)
        ans = 2
        for j in range(1, M):
            if P[j] * P[j-1] < 0:
                ans += 1
            
            
        return ans
        