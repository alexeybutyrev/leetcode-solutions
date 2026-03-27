# Problem: Optimal Partition of String
# Language: python3
# Runtime: 114 ms
# Memory: 14.5 MB

class Solution:
    def partitionString(self, S: str) -> int:
        s = set()
        ans = 0
        for l in S:
            if l in s:
                ans += 1
                s = set()
            s.add(l)
        return ans + 1