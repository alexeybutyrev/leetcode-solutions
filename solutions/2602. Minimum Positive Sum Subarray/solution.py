# Problem: Minimum Positive Sum Subarray 
# Language: python3
# Runtime: 322 ms
# Memory: 16.7 MB

class Solution:
    def minimumSumSubarray(self, A: List[int], l: int, r: int) -> int:
        N = len(A)
        ans = inf
        for i in range(N):
            for j in range(i,N+1):
                L = j - i 
                s = sum(A[i:j])
                if  l <= L <= r and s > 0:
                    ans = min(ans, s)
        return -1 if ans == inf else ans