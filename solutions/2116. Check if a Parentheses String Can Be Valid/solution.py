# Problem: Check if a Parentheses String Can Be Valid
# Language: python3
# Runtime: 189 ms
# Memory: 18.2 MB

class Solution:
    def canBeValid(self, A: str, L: str) -> bool:
        if len(A) % 2 != 0:
            return False
        
        def is_valid(A,L, p):
            bal = wild = 0
            
            for a,l in zip(A,L):
                if l == "1":
                    bal += -1 if a == p else 1
                else:
                    wild += 1
                if bal + wild < 0:
                    return False
                        
            return bal <= wild
        
        c1 = is_valid(A,L, ")")
        c2 = is_valid(A[::-1],L[::-1], "(")
        return c1 and c2
                
                
            
            
            
            
            