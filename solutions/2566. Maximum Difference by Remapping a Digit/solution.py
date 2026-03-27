# Problem: Maximum Difference by Remapping a Digit
# Language: python3
# Runtime: 44 ms
# Memory: 13.9 MB

class Solution:
    def minMaxDifference(self, num: int) -> int:
        S = str(num)
        mx = 0
        mn = inf
        for d1 in range(10):
            for d2 in range(10):
                s1 = S.replace(str(d1),str(d2))
                mx = max(mx, int(s1))
                mn = min(mn, int(s1))
        return mx - mn