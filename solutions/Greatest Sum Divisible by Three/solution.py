# Problem: Greatest Sum Divisible by Three
# Language: python3
# Runtime: 232 ms
# Memory: 19.5 MB

class Solution:
    def maxSumDivThree(self, A: List[int]) -> int:
        N = len(A)
        
        h2 = []
        h1 = []
        
        s2 = 0
        s1 = 0
        s0 = 0
        for a in A:
            c = a % 3
            if c == 2:
                heappush(h2, a)
                s2 += a
            elif c == 1:
                heappush(h1, a)
                s1 += a
            else:
                s0 += a
        
        r = inf
        if (s2 + s1) % 3 == 0:
            return s0 + s1 + s2
        elif (s2 + s1) % 3 == 1:
            
            if len(h1): r = min(r, heappop(h1))
            if len(h2) > 1: r = min(heappop(h2) + heappop(h2),r)
        else:
            if len(h2): r = min(r, heappop(h2))
            if len(h1) > 1: r = min(heappop(h1) + heappop(h1),r)
        return s0 + s1 + s2 - r
        
        
            