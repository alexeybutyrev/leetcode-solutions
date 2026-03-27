# Problem: Check if Grid can be Cut into Sections
# Language: python3
# Runtime: 309 ms
# Memory: 81 MB

class Solution:
    def checkValidCuts(self, n: int, R: List[List[int]]) -> bool:
        N = len(R)
        def check(A):
            c = 0
            x = A[0][1]
            for i in range(1, N):
                if A[i][0] >= x:
                    c += 1
                x = max(x, A[i][1])
            return c >= 2 
        
        # check X
        A = [(sx,ex) for sx,sy,ex,ey in R]
        A.sort(key = lambda x: x[0])

        if check(A): return True
        
        # check Y
        A = [(sy,ey) for sx,sy,ex,ey in R]
        A.sort(key = lambda x: x[0])
        
        
        return check(A)
