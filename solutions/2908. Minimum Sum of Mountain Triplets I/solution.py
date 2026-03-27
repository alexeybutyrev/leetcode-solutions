# Problem: Minimum Sum of Mountain Triplets I
# Language: python3
# Runtime: 47 ms
# Memory: 16.1 MB

class Solution:
    def minimumSum(self, A: List[int]) -> int:
        N = len(A)
        mn = inf
        L = defaultdict(lambda: inf)
        for i in range(N):
            L[i] = mn
            mn = min(mn,A[i])
        
        mn = inf
        R = defaultdict(lambda:inf)
        for i in range(N-1,-1,-1):
            R[i] = mn
            mn = min(mn,A[i])
        
        ans = inf
        for i in range(N):
            if L[i] < A[i]  and A[i] > R[i]:
                ans = min(ans,A[i] + L[i] + R[i])
        return -1 if ans == inf else ans
        