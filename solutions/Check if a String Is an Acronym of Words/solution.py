# Problem: Check if a String Is an Acronym of Words
# Language: python3
# Runtime: 65 ms
# Memory: 16.4 MB

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s): return False
        
        for i in range(len(s)):
            if s[i] != words[i][0]: return False
        return True