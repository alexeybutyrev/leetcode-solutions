# Problem: Minimum Cost Tree From Leaf Values
# Language: python3
# Runtime: 24 ms
# Memory: 14.4 MB

class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res = 0
        while len(A) > 1:
            i = A.index(min(A))
            res += min(A[i - 1:i] + A[i + 1:i + 2]) * A.pop(i)
        return res
        