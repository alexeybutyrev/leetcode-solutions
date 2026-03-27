# Problem: Modify the Matrix
# Language: python3
# Runtime: 74 ms
# Memory: 16.6 MB

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        B = list(zip(*matrix))
        A = [list(x) for x in B]
        for i,x in enumerate(A):
            mx = max(x)
            for j in range(len(A[i])):
                if A[i][j] == -1:
                    A[i][j] = mx
        
        
            
        return list(zip(*A))