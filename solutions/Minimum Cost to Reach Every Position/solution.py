# Problem: Minimum Cost to Reach Every Position
# Language: python3
# Runtime: 4 ms
# Memory: 17.8 MB

class Solution:
    def minCosts(self, A: List[int]) -> List[int]:
        y = A[0]
        ans = []
        ans.append(y)
        for x in A[1:]:
            y = min(y,x)
            ans.append(y)
        return ans