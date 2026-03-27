# Problem: Number of Steps to Reduce a Number to Zero
# Language: python3
# Runtime: 28 ms
# Memory: 13.9 MB

class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0: return 0
        
        count = 0 
        p2 = 1
        
        while p2 <= num:
            if p2 & num !=0:
                count += 2
            else:
                count += 1
            
            p2 *= 2
        
        return count - 1