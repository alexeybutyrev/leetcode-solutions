# Problem: Check If String Is a Prefix of Array
# Language: python3
# Runtime: 36 ms
# Memory: 14.1 MB

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        if s == "":
            return True
        
        W = ""
        for w in words:
            W += w
            if W == s:
                return True
        return False