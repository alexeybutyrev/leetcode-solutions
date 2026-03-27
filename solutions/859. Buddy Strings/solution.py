# Problem: Buddy Strings
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        cA, cB = Counter(A), Counter(B)
        
        if cA != cB:
            return False
        
        if A == B:
            s = 0
            for k,v in cA.items():
                if v > 1:
                    return True
                
            return False
        
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
            if count > 2:
                return False
        
        return True
        
        