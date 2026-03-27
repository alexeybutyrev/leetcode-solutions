# Problem: Apply Bitwise Operations to Make Strings Equal
# Language: python3
# Runtime: 147 ms
# Memory: 14.9 MB

class Solution:
    def makeStringsEqual(self, S: str, T: str) -> bool:
        
        c10 = 0
        c01 = 0
        ct = Counter(T)
        cs = Counter(S)
        for s,t in zip(S,T):
            if s == "1" and t == "0":
                c10 += 1
            
            if s == "0" and t == "1":
                c01 += 1
            
        if c10 and not ct['1']:
            return False
        
        if c01 and not cs['1']:
            return False
        return True