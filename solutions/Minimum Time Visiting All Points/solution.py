# Problem: Minimum Time Visiting All Points
# Language: python3
# Runtime: 1 ms
# Memory: 21.6 MB

class Solution:
    def minTimeToVisitAllPoints(self, A: List[List[int]]) -> int:
        N = len(A)
        @cache
        def move(i,x,y):
            if i == N: return 0
            
            xc, yc = A[i]
            if xc == x and yc == y: return move(i+1,x,y)
            
            
            dx = abs(x-xc)
            dy = abs(y-yc)
            
            return min(dx,dy) + abs(dx-dy) + move(i+1,xc,yc)
        
        return move(0,A[0][0],A[0][1])