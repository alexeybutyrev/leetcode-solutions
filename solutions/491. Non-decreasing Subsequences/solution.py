# Problem: Non-decreasing Subsequences
# Language: python3
# Runtime: 281 ms
# Memory: 22.3 MB

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        N = len(nums)
        def backtrack(A,i):
            if len(A)>1:
                    self.ans.add(tuple(A[:]))
            if i <N:
                
                if nums[i] >= A[-1]:
                    backtrack(A[:] + [nums[i]],i+1)
                backtrack(A[:],i+1)
        
        for i in range(N):
            backtrack([nums[i]],i+1)
        
        return self.ans