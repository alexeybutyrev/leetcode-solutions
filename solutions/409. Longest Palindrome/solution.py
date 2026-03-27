# Problem: Longest Palindrome
# Language: python3
# Runtime: 59 ms
# Memory: 13.9 MB

class Solution:
    def longestPalindrome(self, s: str) -> int:
        mx = 0
        ans = 0
        seen = False
        for k,v in Counter(s).items():
            if v % 2 == 0:
                ans += v
            else:
                ans += v -1
                seen = True
        
        return ans + seen