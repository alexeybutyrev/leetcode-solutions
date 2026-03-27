# Problem: Break a Palindrome
# Language: python3
# Runtime: 24 ms
# Memory: 14.2 MB

class Solution:
    def breakPalindrome(self, s: str) -> str:
        N = len(s)
        if N == 1:
            return ""
        
        s = s.lstrip("a").rstrip("a")
        K = len(s)
        
        if K <= 1:
            return ((N - K) // 2) * 'a' + s + ((N - K) // 2 - 1) * 'a' + 'b'
            
        return ((N - K) // 2) * 'a' + 'a' + s[1:] + ((N - K) // 2) * 'a'
        