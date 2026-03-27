# Problem: Find Indices With Index and Value Difference I
# Language: python3
# Runtime: 57 ms
# Memory: 16.3 MB

class Solution:
    def findIndices(self, A: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        N = len(A)
        for i in range(N):
            for j in range(i,N):
                if j - i >= indexDifference and abs(A[i] - A[j]) >= valueDifference:
                    return [i,j]
        return [-1,-1]