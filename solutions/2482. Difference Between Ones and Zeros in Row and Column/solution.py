# Problem: Difference Between Ones and Zeros in Row and Column
# Language: python3
# Runtime: 1494 ms
# Memory: 52.4 MB

class Solution:
    def onesMinusZeros(self, A: List[List[int]]) -> List[List[int]]:
        OR = []
        ZR = []
        for r in A:
            OR.append(sum(r))
            ZR.append(sum(1 if x == 0 else 0 for x in r))
        
        OC = []
        ZC = []
        for r in zip(*A):
            OC.append(sum(r))
            ZC.append(sum(1 if x == 0 else 0 for x in r))
        
        N = len(A)
        M = len(A[0])
        ANS = [[-1] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                ANS[i][j] = OR[i] + OC[j] - ZR[i] - ZC[j]
        return ANS
        