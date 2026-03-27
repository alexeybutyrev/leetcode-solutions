# Problem: Maximum Value of a String in an Array
# Language: python3
# Runtime: 41 ms
# Memory: 13.9 MB

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for w in strs:
            if w.isnumeric():
                ans = max(ans, int(w))
            else:
                ans = max(ans, len(w))
        return ans