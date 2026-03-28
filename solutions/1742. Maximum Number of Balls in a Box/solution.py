# Problem: Maximum Number of Balls in a Box
# Language: python3
# Runtime: 1008 ms
# Memory: 14.3 MB

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = Counter()
        
        mx = - 1
        for n in range(lowLimit, highLimit + 1):
            s = list(str(n))
            bx = sum(map(int, s))
            c[bx] += 1
            mx = max(mx, c[bx])
       
        
        return mx
            