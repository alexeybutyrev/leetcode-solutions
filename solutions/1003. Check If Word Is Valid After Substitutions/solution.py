# Problem: Check If Word Is Valid After Substitutions
# Language: python3
# Runtime: 28 ms
# Memory: 14.4 MB

class Solution:
    def isValid(self, s: str) -> bool:
        while 'abc' in s:
            s = s.replace('abc','')
        
        return True if not s else False