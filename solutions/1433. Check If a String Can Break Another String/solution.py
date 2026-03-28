# Problem: Check If a String Can Break Another String
# Language: python3
# Runtime: 356 ms
# Memory: 16.2 MB

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        def check(s1,s2):
            l1 = sorted(s1)
            l2 = sorted(s2)

            for i in range(len(l1)):
                if l2[i] < l1[i]:
                    return False

            return True
        
        return bool(check(s1,s2) + check(s2,s1))