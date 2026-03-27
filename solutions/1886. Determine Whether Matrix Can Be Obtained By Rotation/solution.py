# Problem: Determine Whether Matrix Can Be Obtained By Rotation
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def findRotation(self, A: List[List[int]], T: List[List[int]]) -> bool:
        
        def rotate(A):
            N = len(A)
            B = [[0] * N for _ in range(N)]

            for i in range(N):
                for j in range(N):
                    B[i][j] = A[j][i]

            for i,l in enumerate(B):
                B[i] = list(reversed(l))
            return B
        
        B = rotate(A)
        if B == T:
            return True
        
        B = rotate(B)
        if B == T:
            return True
        
        B = rotate(B)
        if B == T:
            return True
        
        B = rotate(B)
        if B == T:
            return True
        
        return False
        