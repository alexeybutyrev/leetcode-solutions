# Problem: Largest Magic Square
# Language: python3
# Runtime: 1874 ms
# Memory: 19.8 MB

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def check(A):
            N = len(A)
            
            S = sum(A[0])
            for x in A:
                sm = sum(x)
                if sm != S: return -1
            for x in list(zip(*A)):
                sm = sum(x)
                if sm != S: return -1
            
            s1 = s2 = 0
            for i in range(N):
                s1 += A[i][i]
                s2 += A[i][N - i - 1]
            return N if S == s1 == s2 else -1
        
        ans = -1
        N, M = len(grid), len(grid[0])
        for xl in range(N):
            for xr in range(xl+1,N+1):
                d = xr - xl
                for yl in range(M):
                    yr = yl + d
                    if yr <= M + 1:
                        A = []
                        for i in range(xl,xr):
                            A.append(grid[i][yl:yr])
                        ans = max(ans, check(A))
        return ans
