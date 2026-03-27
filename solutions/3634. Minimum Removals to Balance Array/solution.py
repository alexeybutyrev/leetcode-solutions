# Problem: Minimum Removals to Balance Array
# Language: python3
# Runtime: 275 ms
# Memory: 43.2 MB

class Solution:
    def minRemoval(self, A: List[int], k: int) -> int:
        A.sort()
        d = {}
        for i,x in enumerate(A):
            ind = bisect_right(A, x * k) - 1
            d[i] = ind

        N = len(A)
        ans = N

        for i in range(N):
            ans = min(ans, i + (N - d[i])-1)
        return ans
