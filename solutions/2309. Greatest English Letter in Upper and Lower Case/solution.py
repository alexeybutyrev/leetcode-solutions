# Problem: Greatest English Letter in Upper and Lower Case
# Language: python3
# Runtime: 26 ms
# Memory: 13.9 MB

class Solution:
    def greatestLetter(self, s: str) -> str:
        for l in 'zyxwvutsrqponmlkjihgfedcba':
            if l in s and l.upper() in s:
                return l.upper()
        return ""