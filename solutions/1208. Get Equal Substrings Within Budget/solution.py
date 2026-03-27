# Problem: Get Equal Substrings Within Budget
# Language: python3
# Runtime: 64 ms
# Memory: 17.2 MB

class Solution:
    def equalSubstring(self, s: str, t: str, C: int) -> int:
        i = 0
        cost_left = C
        ans = 0
        for j in range(len(s)):
            curr = abs(ord(s[j]) - ord(t[j]))
            if curr > cost_left:
                while i <= j and curr > cost_left:
                    cost_left += abs(ord(s[i]) - ord(t[i]))
                    i += 1
            if curr <= cost_left:
                ans = max(ans, j - i + 1)
                cost_left -= curr
        return ans