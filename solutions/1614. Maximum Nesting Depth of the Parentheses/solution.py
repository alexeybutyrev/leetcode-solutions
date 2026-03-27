# Problem: Maximum Nesting Depth of the Parentheses
# Language: python3
# Runtime: 36 ms
# Memory: 14.2 MB

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res = 0
        for l in s:
            if l == "(":
                count += 1
                res = max(count, res)
            if l == ")":
                count -= 1
        return res