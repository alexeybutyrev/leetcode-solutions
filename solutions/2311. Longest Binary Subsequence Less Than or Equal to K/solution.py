# Problem: Longest Binary Subsequence Less Than or Equal to K
# Language: python3
# Runtime: 60 ms
# Memory: 13.9 MB

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        stack = list(s)
        
        ans = 0
        s = ""
        while stack:
            d = stack.pop()
            if d == "0":
                s = "0" + s
            else:
                if int('1' + s,2) <= k:
                    s = "1" + s
            
        return len(s)