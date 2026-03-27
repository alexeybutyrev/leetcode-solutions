# Problem: Count the Hidden Sequences
# Language: python3
# Runtime: 2643 ms
# Memory: 29.3 MB

class Solution:
    def numberOfArrays(self, D: List[int], lo: int, hi: int) -> int:
        
        a = 0
        mx = 0
        mn = 0
        for d in D:
            a += d
            mx = max(a,mx)
            mn = min(a,mn)
        
        delta = mx - mn + 1
        x = hi - lo + 1
        if delta <= x:
            return x - delta + 1
        return 0