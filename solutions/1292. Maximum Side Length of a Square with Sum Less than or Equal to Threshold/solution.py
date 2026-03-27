# Problem: Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# Language: python3
# Runtime: 332 ms
# Memory: 29.1 MB

from itertools import accumulate
class Solution:
    def maxSideLength(self, A: List[List[int]], T: int) -> int:
        N, M = len(A), len(A[0])
        MAT = []
        for x in A:
            MAT.append(list(accumulate(x,initial = 0)))
        A = list( zip(*MAT))
        MAT = []
        for x in A:
            MAT.append(list(accumulate(x,initial = 0)))
        MAT = list(zip(*MAT))
        
        def area(i,j,x):
            #print(i,j,x)
            return MAT[i + x][j + x] + MAT[i][j] - MAT[i+x][j] - MAT[i][j+x]
        
        def check(x):
            for i in range(N):
                for j in range(M):
                    if i + x < N and j + x < M:
                        if area(i,j,x) <= T: return True
                    else:
                        break
            return False
        M += 1
        N += 1
        lo = 0 
        hi = min(N,M)
        while lo < hi:
            mid = lo + hi >> 1

            if check(mid):
                lo = mid + 1
            else:
                hi = mid
            
        return lo-1