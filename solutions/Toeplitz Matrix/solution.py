# Problem: Toeplitz Matrix
# Language: python3
# Runtime: 229 ms
# Memory: 14 MB

class Solution:
    def isToeplitzMatrix(self, A: List[List[int]]) -> bool:
        def check(A):
            N, M = len(A), len(A[0])
            for j in range(M):
                s = set()
                for k in range(max(N,M)):
                    if j + k < M and k < N:
                        s.add(A[k][j+k])
                        if len(s) > 1:
                            return False
                    else:
                        break
            return True
        
        return check(A) and check(list(zip(*A)))
            