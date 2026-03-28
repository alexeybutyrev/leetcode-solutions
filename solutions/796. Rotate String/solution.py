# Problem: Rotate String
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        def leftrotate(s, d):
            return s[d : ] + s[0 : d]
    
        if not A and not B:
            return True
        if len(A) != len(B):
            return False
        
        for i in range(len(A)+1):
            if leftrotate(A, i) == B:
                return True
        return False
            
            