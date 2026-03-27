# Problem: Combination Sum II
# Language: python3
# Runtime: 124 ms
# Memory: 24.9 MB

class Solution:
    def combinationSum2(self, A: List[int], target: int) -> List[List[int]]:
        A.sort()
        N = len(A)
        ans = set()
        @cache
        def dp(i,k,t):
            if k == 0:
                ans.add(t)
            if i < N:
                if A[i] <= k:
                    dp(i+1, k - A[i], tuple(list(t) + [A[i]]))
                dp(i+1, k, t)
        
        dp(0,target,tuple())
        return ans
                
            