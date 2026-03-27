# Problem: Minimum Absolute Sum Difference
# Language: python3
# Runtime: 1557 ms
# Memory: 29.8 MB

class Solution:
    def minAbsoluteSumDiff(self, A: List[int], B: List[int]) -> int:
        
        MOD = 10**9 + 7
        D = [abs(a-b) for a,b in zip(A,B)]
        S = sum(D) 
        A.sort()
        ans = S
        N = len(A)
        for i,d in enumerate(D):
            x = B[i]
            il = bisect_left(A,x)
            il = N - 1 if il == N else il
            ans = min(ans,S - d + abs(A[il] - x))
            
            if il < N - 1:
                ans = min(ans,S - d + abs(A[il+1] - x))
            if il > 0:
                ans = min(ans,S - d + abs(A[il-1] - x))
        
        return ans % MOD
            
        