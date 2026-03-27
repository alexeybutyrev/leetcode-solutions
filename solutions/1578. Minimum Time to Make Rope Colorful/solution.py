# Problem: Minimum Time to Make Rope Colorful
# Language: python3
# Runtime: 35 ms
# Memory: 26.4 MB

class Solution:
    def minCost(self, C: str, T: List[int]) -> int:
        b = "$"
        tb = 0
        ans = 0
        for c,t in zip(C,T):
            if b == c:
                if tb > t:
                    ans += t
                else:
                    ans += tb
                    tb = t
            else:
                tb = t
            b = c
        return ans



