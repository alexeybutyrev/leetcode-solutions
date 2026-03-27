# Problem: Maximize Expression of Three Elements
# Language: python3
# Runtime: 4313 ms
# Memory: 17.7 MB

class Solution:
    def maximizeExpressionOfThree(self, A: List[int]) -> int:
        ans = -inf
        N = len(A)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i != j and i!=k and j !=k:
                        ans = max(ans, A[i] + A[j] - A[k])
        return ans