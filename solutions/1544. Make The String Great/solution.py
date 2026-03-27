# Problem: Make The String Great
# Language: python3
# Runtime: 50 ms
# Memory: 16.6 MB

from string import ascii_lowercase
class Solution:
    def makeGood(self, S: str) -> str:
        s = set()
        for l in ascii_lowercase:
            s.add(l + l.upper())
            s.add(l.upper()+l)
        
        
        while True:
            for l in s:
                if l in S:
                    S = S.replace(l,"")
                    break
            else:
                break
        return S