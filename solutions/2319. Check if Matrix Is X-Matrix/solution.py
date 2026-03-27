# Problem: Check if Matrix Is X-Matrix
# Language: python3
# Runtime: 403 ms
# Memory: 15.1 MB

class Solution:
    def checkXMatrix(self, A: List[List[int]]) -> bool:
        N, M = len(A),len(A[0])

        for i in range(N):
            for j in range(M):
                if i == j or i + j == N-1:
                    if A[i][j] == 0:

                        return False
                else:
                    if A[i][j] != 0:

                        return False
        return True