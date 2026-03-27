# Problem: Get Biggest Three Rhombus Sums in a Grid
# Language: python3
# Runtime: 819 ms
# Memory: 20 MB

class Solution:
    def getBiggestThree(self, A: List[List[int]]) -> List[int]:
        N, M = len(A), len(A[0])
        h = []
        LH = 3
        def add(x):
            if x not in h:
                if len(h) >= LH:
                    x = max(x, heappop(h))
                heappush(h,x)
        
        def check(i,j):
            r = 0
            add(A[i][j])
            r += 1
            while i - r >= 0 and i + r < N and j - r >= 0 and j +r < M:
                s = 0
                # first diag    
                x1,y1 = i - r,j
                x2,y2 = i,j + r
                while x1 != x2 and y1 != y2:
                    s += A[x1][y1]
                    x1 += 1
                    y1 += 1
                # second diag
                x2,y2 = i+r,j
                while x1 != x2 and y1 != y2:
                    s += A[x1][y1]
                    x1 += 1
                    y1 -= 1
                
                # third diag
                x2,y2 = i,j-r
                while x1 != x2 and y1 != y2:
                    s += A[x1][y1]
                    x1 -= 1
                    y1 -= 1
                
                # forth diag
                x2,y2 = i+r,j
                while x1 != x2 and y1 != y2:
                    s += A[x1][y1]
                    x1 -= 1
                    y1 += 1
                
                add(s)
                r += 1
                
            
        for i in range(N):
            for j in range(M):
                check(i,j)
        
        return sorted(h,reverse=True)