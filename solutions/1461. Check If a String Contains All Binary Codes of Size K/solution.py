# Problem: Check If a String Contains All Binary Codes of Size K
# Language: python3
# Runtime: 248 ms
# Memory: 27.5 MB

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        N = len(s)
        c2 = set()
        M = 2 ** k
        for i in range(N - k + 1):
            c2.add(s[i:i+k])
            if len(c2) == M:
                return True
            
        return False
        