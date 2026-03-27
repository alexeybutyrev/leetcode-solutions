# Problem: Remove Palindromic Subsequences
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        N = len(s)
        if not s:
            return 0
        is_pali = lambda x: x == x[::-1]
        
    
        return 1 if is_pali(s) else 2