# Problem: Minimum String Length After Removing Substrings
# Language: python3
# Runtime: 43 ms
# Memory: 16.5 MB

class Solution:
    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            s = s.replace('AB','')
            s = s.replace('CD','')
        return len(s)