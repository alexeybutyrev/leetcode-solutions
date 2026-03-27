# Problem: Maximum Length of Pair Chain
# Language: python3
# Runtime: 241 ms
# Memory: 14.9 MB

class Solution:
    def findLongestChain(self, A: List[List[int]]) -> int:
        
        N = len(A)
        cur, ans = -inf, 0
        for x, y in sorted(A, key = operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans