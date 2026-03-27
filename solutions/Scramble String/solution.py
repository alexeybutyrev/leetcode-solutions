# Problem: Scramble String
# Language: python3
# Runtime: 48 ms
# Memory: 15 MB

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dp(s1,s2):
            if len(s1) != len(s2) or sorted(s1) != sorted(s2): return False
            if len(s1) <  4 or s1 == s2: return True
            for i in range(1,len(s1)):
                if (dp(s1[i:],s2[i:]) and dp(s1[:i],s2[:i])) or (dp(s1[:i],s2[-i:]) and dp(s1[i:],s2[:-i])):
                    return True
            return False
        
        return dp(s1,s2)