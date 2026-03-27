# Problem: Projection Area of 3D Shapes
# Language: python3
# Runtime: 7 ms
# Memory: 19.5 MB

class Solution:
    def projectionArea(self, A: List[List[int]]) -> int:
        X = Counter()
        Y = Counter()
        Z = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                X[i] = max(A[i][j],X[i])
                Y[j] = max(A[i][j],Y[j])
                Z += min(A[i][j],1)
        
        return sum(X.values()) + sum(Y.values()) + Z