# Problem: Pass the Pillow
# Language: python3
# Runtime: 29 ms
# Memory: 13.8 MB

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = 1
        x = 1
        while time:
            
            x += d
            if x == n:
                d *= -1
            elif x == 1:
                d *= -1
            time -=1
        
        return x