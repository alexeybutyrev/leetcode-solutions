# Problem: Maximum Points You Can Obtain from Cards
# Language: python3
# Runtime: 404 ms
# Memory: 27.9 MB

class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        N = len(A)
        sm = sum(A[-k:])
        A = A * 2
        
        ans = sm
        for i in range(k):
            sm += -A[N-k+i] + A[N+i]
            ans = max(ans, sm)
        return ans
            