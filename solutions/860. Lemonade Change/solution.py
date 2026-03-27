# Problem: Lemonade Change
# Language: python3
# Runtime: 124 ms
# Memory: 14.3 MB

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        c5 = 0
        c10 = 0
        
        for b in bills:
            if b == 5:
                c5 += 1
            if b == 10:
                if not c5:
                    return False
                else:
                    c5  -= 1
                    c10 += 1
            if b == 20:
                if not c10:
                    if c5 < 3:
                        return False
                    else:
                        c5 -= 3
                
                else:
                    if c5 == 0:
                        return False
                    c5 -= 1
                    c10 -= 1
                    
                
                    
        return True
    