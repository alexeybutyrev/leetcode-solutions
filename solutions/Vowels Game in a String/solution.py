# Problem: Vowels Game in a String
# Language: python3
# Runtime: 62 ms
# Memory: 18.3 MB

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        a = 0
        b = 0
        for x in s:
            if x in {'a', 'e', 'i', 'o', 'u'}:
                a += 1
            else:
                b += 1
        
        return a != 0
