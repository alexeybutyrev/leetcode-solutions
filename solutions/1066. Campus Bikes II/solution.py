# Problem: Campus Bikes II
# Language: python3
# Runtime: 197 ms
# Memory: 16.3 MB

class Solution:
    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> int:
        dist = lambda x,y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        N = len(W)
        M = len(B)
        target = (1 << N) -1 
        @cache
        def dp(j,mask):
            if mask == target: return 0
            if j == M: return inf
            
            c1 = inf
            for i in range(N):
                if ((1 <<i) & mask) == 0:
                    c1 = min(c1, dist(W[i],B[j]) + dp(j+1, mask | (1<<i)))
            c2 = dp(j + 1,mask)
            return min(c1,c2)
        
        return dp(0,0)
            