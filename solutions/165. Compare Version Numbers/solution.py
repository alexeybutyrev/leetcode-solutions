# Problem: Compare Version Numbers
# Language: python3
# Runtime: 26 ms
# Memory: 16.6 MB

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split(".")[::-1]
        v2 = version2.split(".")[::-1]
        
        while v1 and v2:
            x1 = int(v1.pop())
            x2 = int(v2.pop())
            if x1 < x2:
                return -1
            if x1 > x2:
                return 1
        
        if v1:
            while v1 and int(v1[-1]) == 0:
                v1.pop()
            if not v1:
                return 0
            else:
                return 1
        
        if v2:
            while v2 and int(v2[-1]) == 0:
                v2.pop()
        
        if not v2:
            return 0
        else:
            return -1
        
        
        