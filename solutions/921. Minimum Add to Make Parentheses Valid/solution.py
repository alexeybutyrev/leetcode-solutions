# Problem: Minimum Add to Make Parentheses Valid
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while s and "()" in s:
            s = s.replace("()","")
        
        return len(s)