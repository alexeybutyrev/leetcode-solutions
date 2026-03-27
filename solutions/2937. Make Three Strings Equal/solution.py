# Problem: Make Three Strings Equal
# Language: python3
# Runtime: 60 ms
# Memory: 16.3 MB

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
        L1 = list(s1)
        L2 = list(s2)
        L3 = list(s3)
        
        count = 0
        while max(len(L1),len(L2),len(L3)) >=2:
            if L1 == L2 == L3:
                return count
            if len(L1) >= len(L2) and len(L1) >= len(L3):
                L1.pop()
            elif len(L2) >= len(L1) and len(L2) >= len(L3):
                L2.pop()
            elif len(L3) >= len(L2) and len(L3) >= len(L1):
                L3.pop()
            count += 1
        return count if L1 == L2 == L3 else -1