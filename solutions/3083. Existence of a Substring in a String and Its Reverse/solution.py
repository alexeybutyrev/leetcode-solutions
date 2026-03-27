# Problem: Existence of a Substring in a String and Its Reverse
# Language: python3
# Runtime: 26 ms
# Memory: 16.6 MB

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        N = len(s)
        
        for i in range(1,len(s)):
            if s[i-1:i+1][::-1] in s:
                return True
        return False