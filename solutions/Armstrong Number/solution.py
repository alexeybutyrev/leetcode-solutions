# Problem: Armstrong Number
# Language: python3
# Runtime: 28 ms
# Memory: 14.2 MB

class Solution:
    
    def isArmstrong(self, n: int) -> bool:
        c = Counter(str(n))
        s = 0
        K = len(str(n))
        for k,v in c.items():
            s += v * (int(k)**K)
            if s > n:
                return False
        return s == n