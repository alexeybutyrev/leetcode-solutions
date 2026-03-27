# Problem: Add Minimum Number of Rungs
# Language: python3
# Runtime: 667 ms
# Memory: 28.8 MB

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0
        p = 0
        for r in rungs:
            if r - p > dist:
                c = (r - p) //  dist
                if p + (c - 1) * dist >= r - dist:
                    ans += c-1
                else:
                    ans += c
            p = r
        return ans