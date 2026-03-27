# Problem: Find the Smallest Balanced Index
# Language: python3
# Runtime: 59 ms
# Memory: 32.8 MB


class Solution:
    def smallestBalancedIndex(self, A: list[int]) -> int:
        N = len(A)
        S = sum(A)

        curr = 1
        ans = -1
        p = 1
        s = 0
        for i in range(N-1,-1,-1):
            S -= A[i]
            if S == p:
                ans= i
            elif S < p:
                break
            p *= A[i]
        return ans