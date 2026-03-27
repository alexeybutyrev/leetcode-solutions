# Problem: Minimum Absolute Difference in Sliding Submatrix
# Language: python3
# Runtime: 35 ms
# Memory: 19.4 MB

class Solution:
    def minAbsDiff(self, A: List[List[int]], K: int) -> List[List[int]]:
        N,M = len(A),len(A[0])
        n,m = N-K+1,M-K+1

        ANS = [[inf] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                s = set()
                for x in range(i,i+K):
                    for y in range(j,j+K):
                        s.add(A[x][y])
                if len(s) > 1:
                    B = list(s)
                    B.sort()
                    ANS[i][j] = min(B[j]-B[j-1] for j in range(1,len(B)))
                else:
                    ANS[i][j] = 0
        return ANS