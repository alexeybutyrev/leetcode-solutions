# Problem: Vowels of All Substrings
# Language: python3
# Runtime: 240 ms
# Memory: 15 MB

class Solution:
    def countVowels(self, S: str) -> int:
        N = len(S)
        v = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        dv = 0
        dn = 0
        for i,l in enumerate(S):
            if l in v:
                ans += (i + 1) * (N - i)
                
                
        return ans