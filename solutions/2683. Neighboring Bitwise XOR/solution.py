# Problem: Neighboring Bitwise XOR
# Language: python3
# Runtime: 58 ms
# Memory: 21.8 MB

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        a = 0
        for x in derived[:-1]:
            a = x ^ a
        
        if a == derived[-1] ^ 0: return True
        
        a = 1
        for x in derived[:-1]:
            a = x ^ a
        
        if a == derived[-1] ^ 1: return True
        return False