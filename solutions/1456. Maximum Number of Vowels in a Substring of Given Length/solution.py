# Problem: Maximum Number of Vowels in a Substring of Given Length
# Language: python3
# Runtime: 161 ms
# Memory: 17.3 MB

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        ans = 0
        for i in range(k):
            if s[i] in vowels:
                ans += 1
        
        c = ans
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                c -= 1
            if s[i] in vowels:
                c += 1
            ans = max(ans, c)
        return ans