# Problem: Break a Palindrome
# Language: python3
# Runtime: 32 ms
# Memory: 14.1 MB

class Solution:
    def breakPalindrome(self, s: str) -> str:
        N = len(s)
        
        if N == 1:
            return ""
        
        count = 0
        for i in range(N//2):
            if s[i] == 'a':
                count += 1
            else:
                return s[:count] + "a" + s[count+1:]
        
        return s[:-1] + 'b'
        
        