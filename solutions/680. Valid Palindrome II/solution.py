# Problem: Valid Palindrome II
# Language: python3
# Runtime: 188 ms
# Memory: 14.4 MB

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        is_pali = lambda x: x == x[::-1]
        
        i = 0
        j = (N:=len(s)) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return is_pali(s[i+1:j+1]) or is_pali(s[i:j])
        
        return True