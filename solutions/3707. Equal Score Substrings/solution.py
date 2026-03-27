# Problem: Equal Score Substrings
# Language: python3
# Runtime: 83 ms
# Memory: 17.9 MB

class Solution:
    def scoreBalance(self, S: str) -> bool:
        s1 = 0
        N = len(S)
        def count(S):
            return sum((ord(x) - ord('a') + 1) for x in S)
        for i in range(1,N+1):
            if S[:i] and S[i:] and count(S[:i]) == count(S[i:]): return True
        return False
            
                