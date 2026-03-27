# Problem: Check if Strings Can be Made Equal With Operations I
# Language: python3
# Runtime: 34 ms
# Memory: 16.3 MB

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        l1 = list(s1)
        N = len(s1)
        
        if s1 == s2: return True
        l = l1[:]
        l[0], l[2] = l[2], l[0]
        if "".join(l) == s2: return True
        l[1], l[3] = l[3], l[1]
        if "".join(l) == s2: return True
        l = l1[:]
        l[1], l[3] = l[3], l[1]
        if "".join(l) == s2: return True
        
        return False
        