# Problem: Remove All Occurrences of a Substring
# Language: python3
# Runtime: 28 ms
# Memory: 14.4 MB

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            ind = s.find(part)
            s = s[:ind] + s[ind+len(part):]
        return s