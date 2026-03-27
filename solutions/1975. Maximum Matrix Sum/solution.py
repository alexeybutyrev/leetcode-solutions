# Problem: Maximum Matrix Sum
# Language: python3
# Runtime: 92 ms
# Memory: 26.7 MB

class Solution:
    def maxMatrixSum(self, A: List[List[int]]) -> int:
        
        mn = inf
        sm = 0
        m = 0

        for x in A:
            for y in x:
                if y < 0:
                    m ^= 1
                sm += abs(y)
                mn = min(mn,abs(y))
        if m:
            sm -= 2 * mn
        return sm